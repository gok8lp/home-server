# Tarayıcıdan masaüstü

Üç seçenek, giriş sayfasındaki "Masaüstleri" bölümünden:

| | Ne | Nasıl | Adres |
| --- | --- | --- | --- |
| **Masaüstü** | mullvad-ts sanal makinesi (Eclipse, kalıcı) | Apache Guacamole → RDP (xrdp, Xorg) | `masaustu.<alan-adı>`, evde `<IP>:8097` |
| **Webtop** | kapsayıcıda kalıcı Ubuntu KDE | linuxserver/webtop (Selkies akışı) | `webtop.<alan-adı>` |
| **Kasm** | kullanıp silinen geçici sistemler | linuxserver/kasm (içinde Docker) | `kasm.<alan-adı>`; ilk kurulum `https://<IP>:8102` |

## Guacamole (`yiginlar/guacamole`)

- guacd sunucu ağında (sanal makine ağına ulaşmak için) yalnız Docker köprü adresinde dinler; web arayüzü PostgreSQL
  ile. Bağlantı ayarları `initdb/02-flugel.sql`: 16 bit renk, duvar kâğıdı/saydamlık/menü animasyonu kapalı, ses yok.
- Giriş: kullanıcı `flugel`; internetten TOTP, ev ağı ve Tailscale'den TOTP yok; oturum 1 gün geçerli.
- Şifre değiştirme: `bakim/guac-sifre.sh` (şifre ekranda görünmez, komut satırına yazılmaz).

## Webtop ve Kasm: biri açılınca diğeri kapanır

- `systemd/flugel-webtop.service` ve `flugel-kasm.service` birbirine `Conflicts=`; biri başlayınca systemd diğerini durdurur.
- İkisi de `restart: "no"` ve Docker varsayılan köprü ağında (sunucuda Docker'ın adres havuzu dolu olduğu için).
- Seçim: `yiginlar/anahtar/anahtar.py` (Docker köprüsünde, yalnız yerel) ← giriş sayfasının nginx'i `/anahtar/`
  yolunda HTTP kimlik doğrulamasıyla. Sayfadaki "Aç" düğmesi seçileni başlatır, hazır olunca adrese yönlendirir.
- Webtop/seçim şifresi: `bakim/masaustu-sifre.sh`.

## mullvad-ts oturum davranışı

- **Tek oturum:** aynı kullanıcı için ekran (lightdm) ve web (xrdp) oturumu aynı anda olmaz. Biri açılınca diğerinde
  Eclipse'e "hepsini kaydet" gönderilir, Eclipse düzgün kapatılır, sonra oturum sonlandırılır
  (`vm/mullvad-ts/usr/local/bin/flugel-tek-oturum.sh`, PAM `pam_exec`).
- **Boşta kaydet-kapat:** 15 dk fare/klavye yoksa aynı kaydetme + kapatma, sonra çıkış (`flugel-bosta.timer`,
  dakikada bir). Sanal makine ve VPN kapanmaz.
- **Neden XFCE:** sanal makinede ekran kartı yok; GNOME'un birleştiricisi her kareyi işlemciyle çizdiği için uzak
  masaüstünde takılıyordu. GNOME kurulu duruyor (`ubuntu-xorg` oturumu).
