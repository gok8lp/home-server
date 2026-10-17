# Betikler (otomatik)

Açıklamalar betiklerin baş yorumlarından alınır.

| Dosya | Ne yapar |
| --- | --- |
| `bin/ai-sohbet` | Kullanim: ai-sohbet "konu" [tur_sayisi] [modelA] [modelB] |
| `bin/bildirim` | Merkezi bildirim: Telegram (yapilandirildiysa) + kayit. PC bu kaydi izleyip masaustu bildirimi gosterir. Kullanim: bildirim "mesaj"   \|  bildirim --seviye UYARI "mesaj" |
| `bin/boot-notify.sh` |  |
| `bin/disk-health-report.sh` | Disk sağlık raporu — CallMeBot WhatsApp (akıllandırılmış sürüm) |
| `bin/disk-keepalive.sh` | Fiziksel disk kimligi ile calisir, isim kaymasindan etkilenmez |
| `bin/docker-watcher.sh` |  |
| `bin/emoji-sembol` | Emojileri tek renkli metin simgelerine cevirir (Telegram ve Island bildirimleri icin; kullanici emoji istemiyor). |
| `bin/gpu-bind.sh` |  |
| `bin/gpu-release.sh` | Override'ı temizle |
| `bin/gpu-to-host.sh` | vfio'dan ayır |
| `bin/gpu-to-vm.sh` | Nvidia sürücüsünü ayır |
| `bin/morning-report.sh` | === Rastgele mutlu mesaj === |
| `bin/self-heal.sh` | GPU sanal makinedeyken (W11-GPU, kart vfio-pci'de) bu konteynerler bilerek durdurulur — sorun sayma (sistem-bakim) |
| `bin/smartd-gotify.sh` |  |
| `bin/smartd-whatsapp.sh` |  |
| `bin/ssh-login-watcher.sh` | journalctl follow ile sshd loglarini izle |
| `bin/swap-flush.sh` | Swap kullanımı belirli eşiği geçince, RAM'de yeterli boş alan varsa swap'i temizler (sayfaları RAM'e geri çeker). |
| `bin/telegram-kur` | Telegram bildirim kurulumu (sistem-bakim). Token'i gizli sorar, chat id'yi otomatik bulur. |
| `bin/weekly-maintenance.sh` |  |
| `sbin/ai-gozcu.sh` | AI GOZCU (sistem-bakim): 15 dk'da bir hafif kontrol; sadece YENI sorun cikinca veya gunluk ozette qwen3:8b'ye sorar. Ollama KEEP_ALIVE=0 -> model is bitince GPU'dan bosaltilir (dusuk elektrik). Cikti: ~/sistem-bakim/durum/ |
| `sbin/disk-koruyucu.sh` | OLUM ONCESI KORUMA (sistem-bakim) Her disk icin SMART (5 Reallocated, 187 Uncorrect, 197 Pending, 198 Offline_Uncorrectable, genel saglik) ve kernel I/O hatalarini izler. UYARI: bildirim.  KRITIK: koruma modu -> yazan servisleri durdur, bozulan diski salt-okunur yap, once fotograflari sonra belgeler |
| `sbin/docker-guvenlik-duvari.sh` | Docker'in yayinladigi portlara internetten (fiziksel ag kartindan, ev agi disindan) gelen yeni baglantilari engeller. Ev agi (<IP>/16) ve Tailscale (tailscale0 arayuzu, bu kurala hic girmez) erisebilir. (sistem-bakim) |
| `sbin/flugel-uyari.sh` | FLUGEL Akis: takip edilen kelime gecen yeni haberleri Telegram'a gonderir (sistem-bakim) Kaynak: /opt/stacks/panel/akis/veri/uyari.jsonl (uygulama yazar) · systemd path birimi degisince calistirir |
| `sbin/island-veri.py` | island-veri.py — FLUGEL Island icin hafif sunucu durumu (sistem-bakim, v2). |
| `sbin/kritik-yedek.sh` | Kritik veri yedegi: fotograflar (Immich), Nextcloud, onemli klasorler, sunucu ayarlari -> ikinci fiziksel disk (sdc, /mnt/side) Silinen/degisen dosyalar 30 gun .silinenler/<tarih> altinda tutulur. (sistem-bakim) Kullanim: kritik-yedek.sh [--acil]   (--acil: sadece en onemliler, en hizli sekilde) |
| `sbin/torrent-bekci.sh` | Torrent bekcisi: Transmission'daki tum torrentlerin adini ve dosya listesini yasakli (CSAM) terimlere karsi tarar. Eslesme -> torrent + indirilen veri ANINDA silinir, kayit tutulur. (sistem-bakim) |
| `sbin/virus-tarama.sh` | Indirmeleri ve paylasilan klasorleri ClamAV ile tarar; bulunanlari karantinaya tasir (silmez). (sistem-bakim) |
| `sbin/vm-yonlendir.sh` | vm-yonlendir.sh ekle\|sil <ip>  — Moonlight/Apollo portlarini sunucudan (LAN + Tailscale) Windows VM'e yonlendirir. libvirt hook'u W11 / W11-GPU baslarken "ekle", kapaninca "sil" cagirir. (sistem-bakim) |
| `lib/whatsapp-kapat.sh` |  |
| `bakim/guac-sifre.sh` | Guacamole (tarayıcıdan masaüstü) "flugel" yöneticisinin şifresini koyar. Şifre ekranda görünmez, komut satırına yazılmaz. Guacamole biçimi: hash = SHA-256(şifre + BÜYÜK harf onaltılık tuz) |
| `bakim/kaynak-siniri.py` | kaynak-siniri.py — compose dosyalarına mem_limit ve healthcheck ekler (sistem-bakim v2). |
| `bakim/masaustu-sifre.sh` | Webtop girişi ve ana sayfadaki "masaüstü seç" düğmeleri için şifre (kullanıcı adı: flugel). Şifre ekranda görünmez. |
| `bakim/mullvad-sifre.sh` | mullvad-ts sanal makinesindeki "hello" kullanicisinin sifresini degistirir (makine kapaliyken, disk uzerinden). Sifre ekranda gorunmez; komut satirina yazilmaz (gecici dosya, hemen silinir). |
| `bakim/sunucu-optimizasyon.sh` | flugelserver optimizasyon - her degisiklik yedeklenir ve loglanir Calistirma: scp sunucu-optimizasyon.sh flugelserver:~/sistem-bakim/ && ssh -t flugelserver 'sudo bash ~/sistem-bakim/sunucu-optimizasyon.sh' |
| `bakim/tani-root.sh` | SADECE OKUMA: root gerektiren tani bilgileri. Hicbir ayar degistirmez. |
| `bakim/vmroot.sh` | vmroot.sh KOMUT — mullvad-ts içinde root olarak komut çalıştırır (qemu-guest-agent guest-exec), çıktıyı yazar. |
| `scripts/gmail-auth.py` |  |
| `scripts/gmail-notifier.py` |  |
| `basket-bot/anime_takip.py` | MyAnimeList anime/manga takip botu (sistem-bakim) |
| `basket-bot/ayar.json` |  |
| `basket-bot/basket_bot.py` | Ankara Basketbol fikstur botu (sistem-bakim) |
| `basket-bot/imdb_puan.py` | imdb_puan.py — takip edilen animelerin son bölümünün IMDb puanı (sistem-bakim, FLUGEL Island). |
| `vm/mullvad-ts/usr/local/bin/flugel-bosta.sh` | FLUGEL: masaüstü 15 dk boşta kalınca Eclipse'te her şeyi kaydet, Eclipse'i kapat, oturumu kapat. Boşta: X ekranında 15 dk fare/klavye yok (bağlantı kesilmiş oturum da sayılır). Dakikada bir (flugel-bosta.timer). |
| `vm/mullvad-ts/usr/local/bin/flugel-tek-oturum.sh` | FLUGEL: hello için tek masaüstü oturumu. Biri açılınca (lightdm ekranı ya da xrdp/web) diğer türdeki oturum önce kaydedilir (Eclipse: Ctrl+Shift+S, sonra düzgün kapat) ve sonlandırılır. PAM pam_exec ile root olarak çalışır. |
| `vm/mullvad-ts/root/gnome-kur.sh` | FLUGEL: mullvad-ts'e Ubuntu GNOME masaüstü (xrdp ile). Günlük: /var/log/flugel-gnome.log |
| `vm/mullvad-ts/root/sade.sh` | FLUGEL: mullvad-ts GNOME sadeleştirme/optimizasyon (VPN, ağ, Syncthing, Eclipse dokunulmaz). Günlük: /var/log/flugel-sade.log |
| `vm/mullvad-ts/root/xfce-duzelt.py` |  |
| `vm/mullvad-ts/root/xfce-ubuntu.py` | FLUGEL: hello için Ubuntu görünümlü, hafif XFCE (compositor yok). Mevcut ayarlar yedeklenir. |
