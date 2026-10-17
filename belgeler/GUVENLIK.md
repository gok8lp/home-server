# Güvenlik

## Tehdit modeli

Ev sunucusu; korunan şeyler kişisel fotoğraflar, belgeler ve hesaplar. Başlıca riskler: internetten gelen saldırı,
çalınan hesap/şifre, disk arızası, yanlışlıkla silme, zararlı indirmeler.

## Korumalar

- **Gelen port yok:** internet erişimi Cloudflare tüneliyle; ev yönlendiricisinde port yönlendirme gerekmez.
  Docker portlarına internetten yeni bağlantı `DOCKER-USER` zinciriyle kesilir ([AG-VE-ERISIM.md](AG-VE-ERISIM.md)).
- **Yönetim arayüzleri** (Portainer, Cockpit, Nextcloud, Open WebUI…) Cloudflare Access'in e-posta koduyla korunur.
- **Uzak masaüstü:** Guacamole internetten girişte TOTP ister (ev ağı/Tailscale hariç); 5 hatalı denemede adres
  5 dk engellenir; gerçek istemci adresi `X-Forwarded-For`'dan güvenli vekil listesiyle okunur. Webtop ve masaüstü
  seçimi HTTP kimlik doğrulamasıyla.
- **Disk şifreleme:** üç disk LUKS; sistem diski TPM ile otomatik açılır.
- **Tailscale:** cihazlar arası özel ağ; SSH ve paneller oradan.
- **Zararlılara karşı:** ClamAV haftalık tarama + karantina; torrent bekçisi yasaklı içeriği anında siler.
- **İzleme:** SSH girişleri, kapsayıcı sağlığı, disk sağlığı bildirimleri ([IZLEME-VE-BILDIRIM.md](IZLEME-VE-BILDIRIM.md)).
- **SSH:** root girişi kapalı. Şifreyle giriş açık (yalnız ev ağı ve Tailscale'den erişilebildiği için); anahtar
  zorunluluğu daha güvenli olurdu.

## Bilinçli açıklar (sahibinin kararı)

- Tailscale Funnel ile Jellyfin ve Immich internete açık (kendi girişleri var).
- `adguard.<alan-adı>` DNS kaydı duruyor.

## Bu depodaki temizlik

`temizle.py` depoya giden her dosyada:

- şifre/token/anahtar/salt benzeri değişkenlerin değerini `${DEGISKEN}` yapar (liste: [`env.ornek`](../env.ornek)),
- adresteki `kullanıcı:şifre@` kısmını, Telegram token biçimlerini siler,
- bütün IPv4/IPv6 adreslerini (yerel döngü ve genel DNS hariç) `<IP>`/`<IPv6>` yapar,
- e-postaları, tailnet adını, alan adını ve depo dışındaki listede tutulan diğer kişisel değerleri yer tutucuyla değiştirir.

`guncelle.sh` göndermeden önce bilinen gizli değerleri ve token desenlerini (GitHub, OpenAI, AWS, özel anahtar)
tarar; bir şey bulursa göndermez. `.env` dosyaları, uygulama verileri ve veritabanları hiç toplanmaz.
