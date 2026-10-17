# Sistem servisleri ve zamanlayıcılar (otomatik)

`.service` işi yapar, `.timer` ne zaman çalışacağını, `.path` hangi dosya değişince tetikleneceğini belirler.

| Birim | Açıklama | Ne zaman | Çalıştırdığı | Çakışır |
| --- | --- | --- | --- | --- |
| `ai-gozcu.service` | AI gozcu - sunucu saglik kontrolu |  | `/usr/local/sbin/ai-gozcu.sh` |  |
| `ai-gozcu.timer` | AI gozcu her 15 dakika | açılıştan 3min sonra, sonra her 15min | `` |  |
| `anime-takip.service` | MyAnimeList anime/manga takip botu |  | `/usr/bin/python3 /opt/basket-bot/anime_takip.py` |  |
| `anime-takip.timer` | Anime takip her saat | *-*-* *:05:00 | `` |  |
| `basket-bot.service` | Ankara Basketbol fikstur botu (mac atamalarini takip eder) |  | `/usr/bin/python3 /opt/basket-bot/basket_bot.py` |  |
| `basket-bot.timer` | Basketbol botu her saat basi | *-*-* *:00:00 | `` |  |
| `boot-notify.service` | Notify on boot |  | `/usr/local/bin/boot-notify.sh` |  |
| `cloudflared-akis.service` | cloudflared - FLUGEL Akis (akis.<alan-adı>) |  | `/usr/bin/cloudflared --no-autoupdate --config /etc/cloudflared/akis.yml tunnel run` |  |
| `cloudflared-update.service` | Update cloudflared |  | `/bin/bash -c '/usr/bin/cloudflared update; code=$?; if [ $code -eq 11 ]; then systemctl re` |  |
| `cloudflared-update.timer` | Update cloudflared | daily | `` |  |
| `cloudflared.service` | cloudflared |  | `/usr/bin/cloudflared --no-autoupdate --config /etc/cloudflared/config.yml tunnel run` |  |
| `cpupower-gui.service` |  |  | `` |  |
| `disk-apm.service` | Samsung M3 USB disk APM 254 (kafa park onleme) |  | `/sbin/hdparm -B 254 /dev/disk/by-id/usb-Samsung_M3_Portable_923D7DF202000065-0:0` |  |
| `disk-health.service` | Disk saglik raporu |  | `/usr/local/bin/disk-health-report.sh` |  |
| `disk-health.timer` | Haftalik disk saglik raporu | Sun 10:00 | `` |  |
| `disk-keepalive.service` | Disk sdc keep-alive (park onleme) |  | `/usr/local/bin/disk-keepalive.sh` |  |
| `disk-koruyucu.service` | Olum oncesi disk koruyucu |  | `/usr/local/sbin/disk-koruyucu.sh` |  |
| `disk-koruyucu.timer` | Disk koruyucu her 10 dakika | açılıştan 5min sonra, sonra her 10min | `` |  |
| `docker-guvenlik-duvari.service` | Docker portlarini sadece ev agi ve Tailscale'e ac |  | `/usr/local/sbin/docker-guvenlik-duvari.sh` |  |
| `docker-watcher.service` | Docker kritik durum izleyici |  | `/usr/local/bin/docker-watcher.sh` |  |
| `docker-watcher.timer` | Her 5 dakikada Docker kontrolu | açılıştan 2min sonra, sonra her 5min | `` |  |
| `fix-sudo.service` | Fix sudo setuid bit |  | `/bin/chmod 4755 /usr/bin/sudo.ws` |  |
| `flugel-anahtar.service` | FLUGEL masaustu anahtari (Webtop/Kasm secimi) |  | `/usr/bin/python3 /opt/stacks/anahtar/anahtar.py` |  |
| `flugel-kasm.service` | FLUGEL Kasm (gecici sistemler) |  | `/usr/bin/docker compose up -d` | flugel-webtop.service |
| `flugel-uyari.path` | FLUGEL Akis uyari dosyasini izle (sistem-bakim) | dosya değişince: /opt/stacks/panel/akis/veri/uyari.jsonl | `` |  |
| `flugel-uyari.service` | FLUGEL Akis takip uyarilari -> Telegram (sistem-bakim) |  | `/usr/local/sbin/flugel-uyari.sh` |  |
| `flugel-webtop.service` | FLUGEL Webtop (kalici KDE masaustu) |  | `/usr/bin/docker compose up -d` | flugel-kasm.service |
| `gpu-tasarruf.service` | GTX 1660 Ti tasarruf ayari (persistence + guc siniri) |  | `/bin/sh -c 'nvidia-smi -pm 1; MIN=$(nvidia-smi --query-gpu=power.min_limit --format=csv,no` |  |
| `hd-idle.service` |  |  | `` |  |
| `imdb-puan.service` | FLUGEL Island: takip edilen animelerin son bolum IMDb puani (resmi IMDb veri dosyalari) |  | `/usr/bin/python3 /opt/basket-bot/imdb_puan.py` |  |
| `imdb-puan.timer` | IMDb puanlarini gunde bir guncelle | *-*-* 06:15 | `` |  |
| `iscsi.service` | Login to default iSCSI targets |  | `/usr/lib/open-iscsi/activate-storage.sh` | shutdown.target |
| `island-veri.service` | FLUGEL Island icin sunucu durumu JSON (sistem-bakim) |  | `/usr/local/sbin/island-veri.py` |  |
| `island-veri.timer` | FLUGEL Island sunucu durumu 20 sn (sistem-bakim) | açılıştan 30s sonra, sonra her 20s | `` |  |
| `kritik-yedek.service` | Kritik veri yedegi (fotograf, Nextcloud, ayarlar) -> ikinci disk |  | `/usr/local/sbin/kritik-yedek.sh` |  |
| `kritik-yedek.timer` | Kritik yedek her gece 04:30 | *-*-* 04:30 | `` |  |
| `morning-report.service` | Sabah sunucu raporu |  | `/usr/local/bin/morning-report.sh` |  |
| `morning-report.timer` | Her sabah 07:00 Chicago saati | *-*-* 07:00:00 America/Chicago | `` |  |
| `self-heal.service` | Self-heal: servis/container/disk/ag otomatik onarim |  | `/usr/local/bin/self-heal.sh` |  |
| `self-heal.timer` | Self-heal her 3 dakikada | açılıştan 3min sonra, sonra her 3min | `` |  |
| `ssh-login-watcher.service` | SSH login WhatsApp bildirimi |  | `/usr/local/bin/ssh-login-watcher.sh` |  |
| `swap-flush.service` | Swap kullanimini esik gecince temizle |  | `/usr/local/bin/swap-flush.sh` |  |
| `swap-flush.timer` | swap-flush her 5 dakikada bir calistir | açılıştan 5min sonra, sonra her 5min | `` |  |
| `torrent-bekci.service` | Torrent icerik bekcisi (yasakli icerik filtresi) |  | `/usr/local/sbin/torrent-bekci.sh` |  |
| `torrent-bekci.timer` | Torrent bekcisi her dakika | açılıştan 2min sonra, sonra her 20s | `` |  |
| `virus-tarama.service` | Haftalik virus taramasi |  | `/usr/local/sbin/virus-tarama.sh` |  |
| `virus-tarama.timer` | Virus taramasi her Carsamba 02:00 | Wed *-*-* 02:00 | `` |  |
| `weekly-maintenance.service` | Haftalik bakim |  | `/usr/local/bin/weekly-maintenance.sh` |  |
| `weekly-maintenance.timer` | Pazar 05:00 haftalik bakim | Sun *-*-* 05:00:00 | `` |  |
