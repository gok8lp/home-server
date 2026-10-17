# Yedekleme

## Kritik yedek (her gece 04:30)

`sbin/kritik-yedek.sh` ← `kritik-yedek.timer`. Hedef: ikinci fiziksel disk `/mnt/side/yedek/kritik`.

| Sıra | Kaynak | Not |
| --- | --- | --- |
| 1 | Immich fotoğrafları (`/mnt/sidemain/immich`) | küçük resimler ve yeniden kodlanmış videolar hariç (yeniden üretilebilir) |
| 2 | Nextcloud verisi (`/mnt/sidemain/nextcloud_data`) | |
| 3 | önemli belgeler klasörü | |
| 4 | `/opt/stacks` (yığın ayarları) ve `/etc` | `--acil` kipinde atlanır |

- `rsync -aHAX --delete` ile birebir kopya; **silinen ya da değişen dosyalar** 30 gün boyunca
  `.silinenler/<tarih>` altında tutulur (yanlışlıkla silmeye karşı).
- İki disk de bağlı değilse yedek atlanır ve bildirim gider. Aynı anda iki yedek çalışmaz (kilit dosyası).
- `kritik-yedek.sh --acil`: sadece en önemliler, en hızlı biçimde (disk koruma modu bunu kullanır).

## Diğer koruma katmanları

- **Disk koruma:** bozulan diskten verileri sağlam diske kaçırır ([DEPOLAMA.md](DEPOLAMA.md)).
- **Sanal makine diskleri:** büyük değişikliklerden önce `qcow2` kopyası alınır (ör. mullvad-ts yedeği).
- **Yapılandırma:** bu depo da yapılandırmanın (gizliler hariç) bir kopyasıdır.

## Geri yükleme

```bash
# tek dosya/klasör: yedekten geri kopyala
sudo rsync -aHAX /mnt/side/yedek/kritik/immich/<yol> /mnt/sidemain/immich/<yol>
# yanlışlıkla silinen bir şey: son 30 günün silinenlerinde ara
ls /mnt/side/yedek/kritik/.silinenler/
```

Sınır: yedek aynı binada, aynı elektrik hattında. Yangın/hırsızlığa karşı dışarıda ikinci bir kopya yok.
