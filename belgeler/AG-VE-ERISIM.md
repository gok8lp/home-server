# Ağ ve erişim

## Katmanlar

| Yol | Kimler | Nasıl korunur |
| --- | --- | --- |
| **Ev ağı** (`<IP>/24`) | evdeki cihazlar | yayınlanan Docker portları ve SSH açık |
| **Tailscale** (`<IP>/10`, tailnet `<tailnet>`) | PC, telefon (her yerden) | WireGuard tabanlı özel ağ; `tailscale0` arayüzü güvenlik duvarı kuralına girmez |
| **Cloudflare Tunnel** | internet (okul, misafir) | sunucu dışarıya bağlantı açar, gelen port yok; yönetim adresleri Cloudflare Access (e-posta kodu) arkasında |
| **Tailscale Funnel** | internet | Jellyfin ve Immich için bilerek açık (sahibinin kararı) |

İnternetten sunucuya doğrudan gelen bağlantılar `sbin/docker-guvenlik-duvari.sh` ile engellenir: Docker'ın
yayınladığı portlara fiziksel ağ kartından yalnız ev ağı (`<IP>/16`) yeni bağlantı açabilir (`DOCKER-USER` zinciri).
Docker portları `ufw`'yi atladığı için bu ayrı zincir gerekir.

## İki Cloudflare tüneli

- **Ana tünel (`homeserver`):** Cloudflare panelinden yönetilir (yerel `config.yml`'deki giriş kuralları yok sayılır).
  Kurallar: [`cloudflared/ana-tunel.yml`](../cloudflared/ana-tunel.yml) — Nextcloud, Immich, araçlar, PDF, yapay zekâ,
  dönüştürücü, kitaplar, manga, ofis, Portainer, Cockpit, Jellyfin…
- **Yerel tünel (`flugel-akis`):** sunucudaki [`cloudflared/akis.yml`](../cloudflared/akis.yml) ile yönetilir
  (`cloudflared-akis.service`): giriş sayfası (`<alan-adı>`, `www`), Akış, durum sayfası, masaüstü (Guacamole),
  Webtop, Kasm. Yeni adres: `akis.yml`'ye kural + `cloudflared tunnel route dns flugel-akis <adres>` + servis yeniden başlatma.

Adres → port tablosu: [otomatik/TUNEL.md](otomatik/TUNEL.md) ve [otomatik/YIGINLAR.md](otomatik/YIGINLAR.md)
("Portlar ve erişim" sütunu).

## DNS (AdGuard Home)

Ev ağının DNS'i AdGuard Home (`yiginlar/adguard`). Eskiden `*.<alan-adı>` adreslerini sunucunun yerel IP'sine
çeviren bir yeniden yazma kuralı vardı; yerel ağda 443'te dinleyen olmadığı için evden bütün alt adresleri
bozuyordu, kapatıldı (silinmedi). Artık evden de bütün adresler Cloudflare üzerinden açılır.

## Sanal makine ağı

libvirt `default` NAT ağı ([`libvirt/ag-default.xml`](../libvirt/ag-default.xml)), `<IP>/24`, sabit DHCP:
W11-GPU, W11, mullvad-ts. mullvad-ts ayrıca kendi içinde statik IP kullanır (`vm/mullvad-ts/etc/netplan`).
Windows sanal makinelerine Moonlight/Apollo portları `sbin/vm-yonlendir.sh` ile (libvirt kancası açılış/kapanışta)
sunucudan yönlendirilir.

## Erişim özeti

| Servis | Ev ağı / Tailscale | İnternet |
| --- | --- | --- |
| Giriş sayfası | — | `<alan-adı>` |
| Akış, durum | port 3012, 3004 | tünel |
| Medya, fotoğraf, dosya, ofis, araçlar | portlar | tünel (yönetim olanlar Access arkasında) |
| Guacamole | `<IP>:8097` (çift faktör sorulmaz) | `masaustu.<alan-adı>` (çift faktör) |
| Webtop / Kasm | — / Kasm sihirbazı `https://<IP>:8102` | `webtop.` / `kasm.<alan-adı>` |
| SSH | evet (anahtar + şifre açık) | hayır |
