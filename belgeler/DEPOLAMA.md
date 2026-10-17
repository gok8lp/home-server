# Depolama

| Disk | Boyut | Şifreleme | Bağlama | İçerik |
| --- | --- | --- | --- | --- |
| SSD (`sdb`) | 447 GB | LUKS (TPM ile otomatik açılış) + LVM | `/` | sistem, Docker imajları ve yığın klasörleri, sanal makine diskleri |
| USB Samsung (`sda`) | 931 GB | LUKS | `/mnt/sidemain` | Immich fotoğrafları, Nextcloud verisi, medya kitaplığı, önemli belgeler |
| `sdc` | 466 GB | LUKS | `/mnt/side` | indirmeler, **kritik yedek** (`/mnt/side/yedek/kritik`) |

Ayrıntı: [`sistem/fstab`](../sistem/fstab), [`sistem/crypttab`](../sistem/crypttab), anlık doluluk
[`envanter/SUNUCU.md`](../envanter/SUNUCU.md).

- Veri diskleri `nofail` + 30 sn bekleme ile bağlanır: bir disk takılı değilse sistem yine açılır.
- `noatime,commit=60`: harici disklere daha az yazma.
- Disklerin uyuması: `hd-idle` ve `disk-keepalive` (bkz. [otomatik/SERVISLER.md](otomatik/SERVISLER.md));
  udev kuralları okuma önbelleği ve USB disk güç ayarlarını yapar ([`sistem/udev/rules.d`](../sistem/udev/rules.d)).

## Disk koruma (ölüm öncesi koruma)

`sbin/disk-koruyucu.sh` her diskin SMART değerlerini (5 Reallocated, 187 Uncorrectable, 197 Pending, 198 Offline
Uncorrectable, genel sağlık) ve çekirdek I/O hatalarını izler:

- **Uyarı:** bildirim gönderir.
- **Kritik:** koruma moduna geçer: diske yazan servisleri durdurur, bozulan diski salt okunur yapar, önce
  fotoğrafları sonra belgeleri sağlam diske kopyalar, haber verir ve sunucuyu kapatır. Bir kez tetiklenir; yeniden
  kurmak için `/var/lib/sistem-bakim/koruma-modu` silinir.

`smartd` ([`sistem/smartd.conf`](../sistem/smartd.conf)) ve haftalık disk sağlık raporu
(`bin/disk-health-report.sh`) da çalışır.
