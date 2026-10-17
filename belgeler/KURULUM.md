# Sıfırdan yeniden kurulum

Bu depo gizliler olmadan tutulur; yeniden kurarken `env.ornek`'teki değerler ve şifreler yeniden girilir.

1. **Ubuntu Server** kur (LUKS + LVM). Ağ: [`sistem/netplan`](../sistem/netplan) (IP'yi kendi ağına göre doldur).
2. **Diskler:** veri disklerini LUKS ile aç, [`sistem/crypttab`](../sistem/crypttab) ve
   [`sistem/fstab`](../sistem/fstab) (UUID'leri yeni disklere göre). udev kuralları: [`sistem/udev`](../sistem/udev).
3. **Paketler:** [`envanter/SUNUCU.md`](../envanter/SUNUCU.md) "Elle kurulan paketler" listesi (Docker, libvirt,
   samba, smartmontools, clamav, hd-idle, cloudflared, tailscale, python3…).
4. **Sistem ayarları:** `sistem/` altındaki dosyaları `/etc`'ye (ssh, samba, sysctl, logind, journald, cron,
   modprobe/vfio, GRUB). GPU geçirme için GRUB çekirdek parametreleri ve `vfio.conf`.
5. **Tailscale** ile oturum aç; **Cloudflare:** ana tüneli panelden oluştur, yerel tünel `flugel-akis` için
   `cloudflared tunnel create` + [`cloudflared/akis.yml`](../cloudflared/akis.yml) + `route dns`.
6. **Docker yığınları:** her `yiginlar/<ad>/compose.yaml` → `/opt/stacks/<ad>/`; gizli değerler için o klasörde
   `.env` (hangi değişken: `env.ornek`). Sıra: adguard → gluetun → nextcloud/immich → medya → panel → uzak masaüstü.
   Not: depodaki dosyalarda `<IP>` / `<alan-adı>` yer tutucuları var, gerçek değerlerle değiştir.
7. **Betikler ve servisler:** `bin/` → `/usr/local/bin`, `sbin/` → `/usr/local/sbin`, `lib/` →
   `/usr/local/lib/sistem-bakim`, `systemd/` → `/etc/systemd/system`; `systemctl daemon-reload` ve zamanlayıcıları etkinleştir.
   Bildirim için Telegram/CallMeBot anahtarları.
8. **Sanal makineler:** `libvirt/vm/*.xml` → `virsh define`, ağ `libvirt/ag-default.xml`, kanca `libvirt/qemu-hook`
   → `/etc/libvirt/hooks/qemu`. mullvad-ts içi: `vm/mullvad-ts/`.
9. **Yedeği geri yükle:** `/mnt/side/yedek/kritik` → `/mnt/sidemain` ([YEDEKLEME.md](YEDEKLEME.md)).
