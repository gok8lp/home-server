# home-server

Kişisel ev sunucumun (flugelserver) tüm yapısı: sistem ayarları, Docker yığınları, servisler, betikler, botlar,
Cloudflare tünelleri ve sanal makineler. *My home server as code: system config, Docker stacks, services, scripts,
bots, tunnels and VMs (Turkish).*

> Bu depo canlı sistemin **temizlenmiş kopyasıdır**. Şifre, token ve anahtarlar `${DEGISKEN}` yer tutucusuna,
> IP adresleri `<IP>`, alan adı `<alan-adı>`, tailnet `<tailnet>`, e-postalar `<e-posta>` olur. `.env`
> dosyaları, uygulama verileri ve veritabanları hiç alınmaz. Dosyalar olduğu gibi kopyalanıp çalıştırılmamalı.

## Donanım ve sistem

Ryzen 5 2600X, 15 GB RAM, GTX 1660 Ti (sanal makineye geçirilebilir), SSD + iki harici disk; Ubuntu 26.04,
Docker, libvirt/KVM, Tailscale, Cloudflare Tunnel. Ayrıntılı anlık envanter: [`envanter/SUNUCU.md`](envanter/SUNUCU.md).

## Klasörler

| Klasör | İçerik |
| --- | --- |
| `sistem/` | `/etc` ayarları: ağ (netplan), diskler (fstab, crypttab, udev, hd-idle), Samba, smartd, Docker daemon, SSH, ufw, GRUB/VFIO, sysctl, cron, logind/journald, Apache |
| `yiginlar/` | Docker yığınları (compose + yapılandırma): adguard ai-sandbox anahtar bazarr code-server convertx daedalos filebrowser flaresolverr giris gluetun gotify guacamole immich_server it-tools jackett kamiyomu kasm kavita komga libreoffice lingarr n8n netdata nextcloud openbooks prowlarr radarr sonarr stirling-pdf subgen tapmap tranga-api transmission2 uptime-kuma webtop  |
| `panel/` | Homepage paneli, FLUGEL Akış (kişisel haber/oyun/anime akışı), gündem botu |
| `basket-bot/` | basketbol hakem görev botu, anime takip, IMDb puanı |
| `systemd/` | sunucuya özel servis/zamanlayıcı/yol birimleri (izleme, yedek, güvenlik duvarı, Island verisi, Webtop/Kasm seçimi…) |
| `bin/`, `sbin/`, `lib/` | bildirim (Telegram/WhatsApp/Gotify), sabah raporu, disk sağlığı, kendini onarma, kritik yedek, virüs tarama, torrent bekçisi |
| `bakim/` | bakım yardımcıları: sanal makinede root komutu (qemu-guest-agent), şifre koyma betikleri |
| `scripts/` | Gmail bildirici |
| `cloudflared/` | Cloudflare tünel giriş kuralları |
| `libvirt/` | GPU geçirme kancası, sanal makine tanımları (`vm/`), sanal ağ |
| `vm/mullvad-ts/` | VPN + tarayıcıdan geliştirme masaüstü sanal makinesi: ağ, xrdp, ekran yöneticisi, tek oturum ve boşta kaydet-kapat betikleri, XFCE düzeni |
| `envanter/` | donanım, diskler, kapsayıcılar, sanal makineler, servisler, paketler |
| `env.ornek` | depodan çıkarılan gizli değişkenlerin listesi ve kullanıldıkları dosyalar |

## Öne çıkanlar

- **Tarayıcıdan masaüstü:** Apache Guacamole (sanal makineye RDP, internetten girişte TOTP), Webtop (Ubuntu KDE) ve
  Kasm (geçici sistemler); Webtop ve Kasm systemd `Conflicts` ile aynı anda çalışmaz, giriş sayfasındaki düğmelerle seçilir.
- **Giriş sayfası:** tek statik sayfada bütün servisler (`yiginlar/giris/`).
- **GPU'lu Windows sanal makinesi:** libvirt kancası GTX 1660 Ti'yi açılışta sanal makineye, kapanışta sunucuya verir.
- **İzleme ve bildirim:** disk sağlığı, Docker durumu, SSH girişleri, kendini onarma, yapay zekâ destekli sorun özeti.

## Güncelleme

```bash
./guncelle.sh "açıklama"
```

`topla.sh` sunucudan toplar ve `temizle.py` ile temizler (kişisel değerler depo dışındaki yerel listede);
`guncelle.sh` gizli bilgi taraması yapar, bulursa göndermez.
