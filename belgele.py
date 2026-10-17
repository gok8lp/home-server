#!/usr/bin/env python3
"""Depodaki dosyalardan ayrıntılı belgeler üretir (belgeler/otomatik/*.md). topla.sh her toplamada çağırır."""
import os, re, glob, configparser, xml.etree.ElementTree as ET
import yaml

R = os.path.dirname(os.path.abspath(__file__))
O = os.path.join(R, "belgeler", "otomatik"); os.makedirs(O, exist_ok=True)
def oku(p):
    try: return open(p, encoding="utf-8").read()
    except Exception: return ""
def yaz(ad, metin): open(os.path.join(O, ad), "w", encoding="utf-8").write(metin.rstrip() + "\n")
def hucre(x): return str(x).replace("|", "\\|").replace("\n", " ")

# ---------- tünel adresleri ----------
tunel = {}
for p in glob.glob(os.path.join(R, "cloudflared", "*.yml")):
    try: d = yaml.safe_load(oku(p)) or {}
    except Exception: continue
    for k in d.get("ingress", []) or []:
        if k.get("hostname"):
            m = re.search(r":(\d+)", str(k.get("service", "")))
            if m: tunel.setdefault(m.group(1), []).append(k["hostname"])

# ---------- Docker yığınları ----------
satirlar, ayrinti = [], []
for f in sorted(glob.glob(os.path.join(R, "yiginlar", "*", "*compose*.y*ml")) + glob.glob(os.path.join(R, "panel", "compose.yaml"))):
    yigin = os.path.basename(os.path.dirname(f)); metin = oku(f)
    aciklama = " ".join(l.lstrip("# ").strip() for l in metin.splitlines()[:3] if l.startswith("#"))[:220]
    try: d = yaml.safe_load(metin) or {}
    except Exception as e:
        satirlar.append(f"| `{yigin}` | (okunamadı) | | | | |"); continue
    ayrinti.append(f"\n### `{yigin}`\n\nDosya: `{os.path.relpath(f, R)}`" + (f"\n\n{aciklama}" if aciklama else ""))
    for ad, s in (d.get("services") or {}).items():
        s = s or {}
        portlar = [str(p) for p in s.get("ports", []) or []]
        dis = []
        for p in portlar:
            m = re.match(r"(?:(\S+?):)?(\d+):\d+", p.replace('"', ''))
            if m:
                bag, hp = m.group(1) or "0.0.0.0", m.group(2)
                yol = ("yalnız sunucu içi" if bag.startswith("127.") else "ev ağı + Tailscale")
                if hp in tunel: yol += " + internet (" + ", ".join(tunel[hp]) + ")"
                dis.append(f"{hp} ({yol})")
        if s.get("network_mode") == "host": dis.append("sunucu ağı (host)")
        bellek = s.get("mem_limit") or (((s.get("deploy") or {}).get("resources") or {}).get("limits") or {}).get("memory") or ""
        hacim = [str(v).split(":")[0] for v in s.get("volumes", []) or []]
        satirlar.append(f"| `{yigin}` | `{ad}` | `{hucre(s.get('image', s.get('build', '')))}` | {hucre('; '.join(dis))} | {hucre(bellek)} | {hucre(s.get('restart', ''))} |")
        ayrinti.append(f"\n- **{ad}**: imaj `{s.get('image', s.get('build', ''))}`"
                       + (f", portlar: {', '.join(portlar)}" if portlar else "")
                       + (f", ağ: {s.get('network_mode')}" if s.get('network_mode') else "")
                       + (f", bellek sınırı: {bellek}" if bellek else "")
                       + (f", ayrıcalıklı" if s.get('privileged') else "")
                       + (f"\n  - bağlı klasörler: {', '.join('`'+h+'`' for h in hacim)}" if hacim else "")
                       + (f"\n  - ortam değişkenleri: {', '.join('`'+(k if isinstance(s['environment'], dict) else str(k).split('=')[0])+'`' for k in (s['environment'] if isinstance(s['environment'], (dict, list)) else []))}" if s.get('environment') else ""))
yaz("YIGINLAR.md", "# Docker yığınları (otomatik)\n\nHer satır bir kapsayıcı. *Dışarıya açılma*: `127.0.0.1` bağlı portlar yalnız sunucu içinden; "
    "diğerleri ev ağı ve Tailscale'den (güvenlik duvarı internetten gelen yeni bağlantıları keser); tünel adresi olanlar Cloudflare ile internetten.\n\n"
    "| Yığın | Servis | İmaj | Portlar ve erişim | Bellek | Yeniden başlatma |\n| --- | --- | --- | --- | --- | --- |\n" + "\n".join(satirlar)
    + "\n\n## Ayrıntı\n" + "\n".join(ayrinti))

# ---------- systemd ----------
def birim(p):
    c = configparser.ConfigParser(strict=False, interpolation=None, allow_no_value=True); c.optionxform = str
    try: c.read_string(oku(p))
    except Exception: return {}
    return {b: dict(c[b]) for b in c.sections()}
satir = []
for p in sorted(glob.glob(os.path.join(R, "systemd", "*"))):
    ad = os.path.basename(p); b = birim(p)
    u, sv, tm, pt = b.get("Unit", {}), b.get("Service", {}), b.get("Timer", {}), b.get("Path", {})
    ne = sv.get("ExecStart", "") or ""
    zaman = tm.get("OnCalendar") or (("açılıştan " + tm["OnBootSec"]) if tm.get("OnBootSec") else "") or (("her " + tm["OnUnitActiveSec"]) if tm.get("OnUnitActiveSec") else "")
    if tm.get("OnUnitActiveSec") and tm.get("OnBootSec"): zaman = f"açılıştan {tm['OnBootSec']} sonra, sonra her {tm['OnUnitActiveSec']}"
    if pt: zaman = "dosya değişince: " + (pt.get("PathModified") or pt.get("PathChanged") or "")
    satir.append(f"| `{ad}` | {hucre(u.get('Description', ''))} | {hucre(zaman)} | `{hucre(ne)[:90]}` | {hucre(u.get('Conflicts', ''))} |")
yaz("SERVISLER.md", "# Sistem servisleri ve zamanlayıcılar (otomatik)\n\n`.service` işi yapar, `.timer` ne zaman çalışacağını, `.path` hangi dosya değişince tetikleneceğini belirler.\n\n"
    "| Birim | Açıklama | Ne zaman | Çalıştırdığı | Çakışır |\n| --- | --- | --- | --- | --- |\n" + "\n".join(satir))

# ---------- betikler ----------
satir = []
for k in ["bin", "sbin", "lib", "bakim", "scripts", "basket-bot", "vm/mullvad-ts/usr/local/bin", "vm/mullvad-ts/root"]:
    for p in sorted(glob.glob(os.path.join(R, k, "*"))):
        if os.path.isdir(p): continue
        m = oku(p).splitlines()
        aciklama = []
        for l in m[1:14]:
            l2 = l.strip()
            if l2.startswith("#") and not l2.startswith("#!") and len(l2) > 3: aciklama.append(l2.lstrip("# ").strip())
            elif l2.startswith('"""') or l2.startswith("'''"): aciklama.append(l2.strip("\"' ")); 
            elif aciklama: break
        satir.append(f"| `{os.path.relpath(p, R)}` | {hucre(' '.join(aciklama))[:300]} |")
yaz("BETIKLER.md", "# Betikler (otomatik)\n\nAçıklamalar betiklerin baş yorumlarından alınır.\n\n| Dosya | Ne yapar |\n| --- | --- |\n" + "\n".join(satir))

# ---------- sanal makineler ----------
bol = []
for p in sorted(glob.glob(os.path.join(R, "libvirt", "vm", "*.xml"))):
    try: x = ET.fromstring(oku(p))
    except Exception: continue
    ad = x.findtext("name"); bellek = int(x.findtext("memory") or 0) // 1024
    disk = [(d.find("source").get("file") if d.find("source") is not None else "", d.find("target").get("dev") if d.find("target") is not None else "") for d in x.findall("./devices/disk")]
    hd = len(x.findall("./devices/hostdev")); ag = [i.get("type") for i in x.findall("./devices/interface")]
    gr = [g.get("type") for g in x.findall("./devices/graphics")]
    os_ = x.find(".//{http://libosinfo.org/xmlns/libvirt/domain/1.0}os")
    bol.append(f"\n## {ad}\n\n- İşletim sistemi: {os_.get('id') if os_ is not None else '?'}\n- İşlemci: {x.findtext('vcpu')} sanal çekirdek, bellek: {bellek} MB\n"
               f"- Diskler: {', '.join(f'`{s}` ({t})' for s, t in disk)}\n- Ağ: {', '.join(ag)}; ekran: {', '.join(gr) or 'yok'}\n"
               f"- Doğrudan aktarılan donanım (PCI/USB): {hd}" + (" (GPU geçirme)" if hd else ""))
yaz("SANAL-MAKINELER.md", "# Sanal makineler (otomatik)\n\nlibvirt/KVM tanımlarından.\n" + "".join(bol))

# ---------- tünel ----------
satir = [f"| {h} | {p} |" for p, hs in sorted(tunel.items()) for h in hs]
yaz("TUNEL.md", "# Cloudflare tünel adresleri (otomatik, yerel tünel)\n\nAna tünel Cloudflare panelinden yönetilir; buradaki tablo sunucudaki yerel tünel dosyasından.\n\n| Adres | Sunucu portu |\n| --- | --- |\n" + "\n".join(satir))
print("belgeler üretildi:", ", ".join(sorted(os.listdir(O))))
