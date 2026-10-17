# İzleme ve bildirim

## Bildirim kanalları

- **`bin/bildirim`**: merkezi bildirim. Telegram'a (yapılandırıldıysa) gönderir ve kayda yazar; PC'deki FLUGEL Island
  bu kaydı izleyip masaüstü bildirimi ve kapsülde canlı etkinlik gösterir. Emojiler tek renkli simgelere çevrilir
  (`bin/emoji-sembol`). Seviyeler: BİLGİ, UYARI, HATA.
- **WhatsApp (CallMeBot)**: eski raporlar (`smartd-whatsapp.sh`, sabah ve haftalık raporlar, Docker izleyici).
- **Gotify**: kendi barındırılan bildirim sunucusu (`yiginlar/gotify`), smartd ile kullanılır.

## İzleyiciler

| Ne | Nasıl | Sıklık |
| --- | --- | --- |
| Kendini onarma (`bin/self-heal.sh`) | düşen kritik servisleri kaldırır, hatayla çıkan kapsayıcıları yeniden başlatır, 10 dk boyunca sağlıksız kalanı yeniden başlatır, disk %90'ı geçerse temizlik | 3 dk |
| Docker izleyici (`bin/docker-watcher.sh`) | yeni sağlıksız, hatayla çıkan ve yeniden başlama döngüsündeki kapsayıcıları bildirir (çıkış kodunu yorumlar) | 5 dk |
| Disk koruyucu (`sbin/disk-koruyucu.sh`) | SMART + çekirdek I/O hataları; kritikte koruma modu | 10 dk |
| AI gözcü (`sbin/ai-gozcu.sh`) | hafif kontroller; yalnız yeni sorun çıkınca ya da günlük özette yerel modele (Ollama, qwen3:8b) sorar, Türkçe açıklama ve güvenli çözüm önerisi üretir; model iş bitince GPU'dan boşaltılır | 15 dk |
| SSH giriş izleyici (`bin/ssh-login-watcher.sh`) | sshd günlüğünü izler; bilinen ağlar (ev, Tailscale) dışındaki girişleri bildirir | sürekli |
| Swap boşaltma (`bin/swap-flush.sh`) | swap eşiği geçince ve RAM yeterliyse sayfaları RAM'e çeker | 5 dk |
| Torrent bekçisi (`sbin/torrent-bekci.sh`) | Transmission'daki torrent adlarını ve dosya listelerini yasaklı (CSAM) terimlere karşı tarar; eşleşmeyi verisiyle birlikte anında siler, kayıt tutar | 20 sn |
| Virüs tarama (`sbin/virus-tarama.sh`) | indirmeleri ve paylaşılan klasörleri ClamAV ile tarar, bulunanları karantinaya alır (silmez) | Çarşamba 02:00 |
| Disk sağlık raporu | SMART özeti | Pazar 10:00 |
| Haftalık bakım (`bin/weekly-maintenance.sh`) | `apt` güncelleme + yükseltme + autoremove, kullanılmayan Docker imajlarını silme, günlükleri 14 güne indirme, SSD trim; özet WhatsApp'a | Pazar 05:00 |
| Sabah raporu (`bin/morning-report.sh`) | yük, RAM, swap, disk, sıcaklık özeti | her gün* |
| Açılış bildirimi (`bin/boot-notify.sh`) | sunucu açılınca haber verir | açılışta |

\* Zamanlayıcı `07:00 America/Chicago` yazılı; Türkiye saatiyle 15:00'e denk geliyor. Sabah gelmesi isteniyorsa
`Europe/Istanbul` yapılmalı (değiştirilmedi).

Ayrıca: Uptime Kuma (`yiginlar/uptime-kuma`, `status.<alan-adı>`), Netdata (`yiginlar/netdata`, canlı grafikler),
Homepage paneli (`panel/homepage`).

## FLUGEL Island verisi

`sbin/island-veri.py` (20 sn): CPU, sıcaklık, RAM, swap, diskler, GPU, kapsayıcı sayısı ve sağlıksızlar, VPN,
Ollama, yedek durumu, sanal makineler, son uyarılar, basket görevleri, anime takvimi → JSON. FLUGEL Akış bunu
`/api/island` olarak verir; PC'deki GNOME eklentisi ve üst çubuk okur. Takip edilen kelime geçen yeni haberler
`sbin/flugel-uyari.sh` ile (yol birimi, dosya değişince) Telegram'a gider.
