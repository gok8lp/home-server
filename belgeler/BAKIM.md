# Bakım ve sorun giderme

## Bu depoyu güncelleme

```bash
./guncelle.sh "açıklama"     # topla.sh → temizle.py → belgele.py → gizli taraması → commit → push
```

## Sık işler

| İş | Komut |
| --- | --- |
| Kapsayıcı durumu | `docker ps --format 'table {{.Names}}\t{{.Status}}'` |
| Bir yığını yeniden başlat | `cd /opt/stacks/<ad> && docker compose up -d` |
| Servis/zamanlayıcı durumu | `systemctl list-timers` · `systemctl status <ad>` |
| Son bildirimler | `bin/bildirim` betiğinin yazdığı kayıt dosyası (betikte tanımlı yol) |
| Webtop ↔ Kasm | giriş sayfasındaki "Aç" ya da `sudo systemctl start flugel-webtop` / `flugel-kasm` |
| mullvad-ts içinde root komutu | `~/sistem-bakim/vmroot.sh 'komut'` |
| Sanal makineyi düzgün kapat/aç | `sudo virsh shutdown <ad>` / `sudo virsh start <ad>` (asla `destroy`) |
| Kritik yedeği elle çalıştır | `sudo systemctl start kritik-yedek` |
| Disk koruma modunu sıfırla | `sudo rm /var/lib/sistem-bakim/koruma-modu` |

## Bilinen tuzaklar

- **Docker adres havuzu dolu:** yeni yığın ağ oluşturamazsa (`all predefined address pools have been fully
  subnetted`) ya `network_mode: bridge` kullan ya da `/etc/docker/daemon.json`'a `default-address-pools` ekle
  (ikincisi Docker'ı yeniden başlatmayı gerektirir).
- **Ana tünel** panelden yönetilir; yerel `config.yml` kuralları etkisizdir.
- **GPU sanal makinedeyken** Ollama/Whisper bilerek durur.
- **mullvad-ts IP'si** statik; değiştirirsen Guacamole bağlantısını da güncelle.
- **Depodaki dosyalar** yer tutuculu; canlı sisteme depodan doğrudan kopyalama (özellikle `panel/akis`).
