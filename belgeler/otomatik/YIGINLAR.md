# Docker yığınları (otomatik)

Her satır bir kapsayıcı. *Dışarıya açılma*: `127.0.0.1` bağlı portlar yalnız sunucu içinden; diğerleri ev ağı ve Tailscale'den (güvenlik duvarı internetten gelen yeni bağlantıları keser); tünel adresi olanlar Cloudflare ile internetten.

| Yığın | Servis | İmaj | Portlar ve erişim | Bellek | Yeniden başlatma |
| --- | --- | --- | --- | --- | --- |
| `panel` | `homepage` | `ghcr.io/gethomepage/homepage:latest` | 3010 (ev ağı + Tailscale) | 384m | unless-stopped |
| `panel` | `gundem-botu` | `python:3.13-alpine` | 3011 (ev ağı + Tailscale) | 128m | unless-stopped |
| `panel` | `flugel-akis` | `python:3.13-alpine` | 3012 (ev ağı + Tailscale + internet (akis.<alan-adı>)) | 512m | unless-stopped |
| `adguard` | `adguardhome` | `adguard/adguardhome` | 53 (ev ağı + Tailscale); 53 (ev ağı + Tailscale); 53 (ev ağı + Tailscale); 53 (ev ağı + Tailscale); 3000 (ev ağı + Tailscale); 8888 (ev ağı + Tailscale + internet (adguard.<alan-adı>)); 853 (ev ağı + Tailscale); 853 (ev ağı + Tailscale) | 768m | unless-stopped |
| `ai-sandbox` | `sohbet` | `python:3.12-alpine` |  | 256m | no |
| `bazarr` | `bazarr` | `lscr.io/linuxserver/bazarr:latest` | 6767 (ev ağı + Tailscale) | 1g | unless-stopped |
| `code-server` | `code-server` | `lscr.io/linuxserver/code-server:latest` | 8444 (ev ağı + Tailscale + internet (code.<alan-adı>)) | 1536m | unless-stopped |
| `convertx` | `convertx` | `ghcr.io/c4illin/convertx` | 3003 (ev ağı + Tailscale + internet (convert.<alan-adı>)) | 2g | unless-stopped |
| `daedalos` | `daedalos` | `{'context': 'https://github.com/DustinBrett/daedalOS.git#main', 'dockerfile': 'Dockerfile'}` | 3005 (ev ağı + Tailscale + internet (ui.<alan-adı>)) | 1G | unless-stopped |
| `filebrowser` | `filebrowser` | `filebrowser/filebrowser:latest` | 8085 (ev ağı + Tailscale + internet (files.<alan-adı>)) |  | unless-stopped |
| `flaresolverr` | `flaresolverr` | `ghcr.io/flaresolverr/flaresolverr:latest` |  | 1536m | unless-stopped |
| `giris` | `giris` | `nginx:1.27-alpine` | 8098 (yalnız sunucu içi + internet (<alan-adı>, www.<alan-adı>)) | 32m | unless-stopped |
| `gluetun` | `gluetun` | `qmcgaw/gluetun` | 8889 (ev ağı + Tailscale); 9091 (ev ağı + Tailscale); 51413 (ev ağı + Tailscale); 51413 (ev ağı + Tailscale); 9696 (ev ağı + Tailscale) | 256m | unless-stopped |
| `gotify` | `gotify` | `gotify/server:latest` | 8482 (ev ağı + Tailscale) |  | unless-stopped |
| `guacamole` | (okunamadı) | | | | |
| `immich_server` | `immich-server` | `ghcr.io/immich-app/immich-server:release` | 2283 (ev ağı + Tailscale + internet (immich.<alan-adı>, immich.<alan-adı>)) | 3g | unless-stopped |
| `immich_server` | `immich-machine-learning` | `ghcr.io/immich-app/immich-machine-learning:release-cuda` |  | 2g | unless-stopped |
| `immich_server` | `redis` | `docker.io/redis:6.2-alpine` |  | 256m | unless-stopped |
| `immich_server` | `database` | `ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0` |  | 1536m | unless-stopped |
| `it-tools` | `it-tools` | `corentinth/it-tools:latest` | 8233 (ev ağı + Tailscale + internet (tools.<alan-adı>, tools.<alan-adı>)) | 256m | unless-stopped |
| `jackett` | `jackett` | `lscr.io/linuxserver/jackett:latest` | 9117 (ev ağı + Tailscale) | 512m | unless-stopped |
| `kamiyomu` | `kamiyomu` | `marcoscostadev/kamiyomu:latest` | 2342 (ev ağı + Tailscale) | 1g | unless-stopped |
| `kasm` | `kasm` | `lscr.io/linuxserver/kasm:latest` | 8102 (ev ağı + Tailscale); 8103 (yalnız sunucu içi + internet (kasm.<alan-adı>)) |  | no |
| `kavita` | `kavita` | `lscr.io/linuxserver/kavita:latest` | 8295 (ev ağı + Tailscale + internet (ln.<alan-adı>)) | 768m | unless-stopped |
| `komga` | `komga` | `gotson/komga:latest` | 8296 (ev ağı + Tailscale + internet (manga.<alan-adı>)) | 1536m | unless-stopped |
| `libreoffice` | `libreoffice` | `lscr.io/linuxserver/libreoffice:latest` | 3205 (ev ağı + Tailscale + internet (office.<alan-adı>)); 3206 (ev ağı + Tailscale) | 1536m | unless-stopped |
| `lingarr` | `lingarr` | `ghcr.io/lingarr-translate/lingarr:latest` | 5575 (ev ağı + Tailscale) | 512m | unless-stopped |
| `n8n` | `n8n` | `n8nio/n8n:latest` | 5678 (ev ağı + Tailscale) | 1g | unless-stopped |
| `netdata` | `netdata` | `netdata/netdata:latest` | 19999 (ev ağı + Tailscale) | 768m | unless-stopped |
| `nextcloud` | `nextcloud` | `lscr.io/linuxserver/nextcloud:latest` | 8443 (yalnız sunucu içi + internet (nextcloud.<alan-adı>, nextcloud.<alan-adı>)); 8443 (ev ağı + Tailscale + internet (nextcloud.<alan-adı>, nextcloud.<alan-adı>)) | 1536m | unless-stopped |
| `openbooks` | `openbooks` | `evanbuss/openbooks:latest` | 8285 (ev ağı + Tailscale + internet (bd.<alan-adı>)) | 256m | unless-stopped |
| `prowlarr` | `prowlarr` | `lscr.io/linuxserver/prowlarr:latest` |  | 512m | unless-stopped |
| `radarr` | `radarr` | `lscr.io/linuxserver/radarr:latest` | 7878 (ev ağı + Tailscale) | 768m | unless-stopped |
| `sonarr` | `sonarr` | `lscr.io/linuxserver/sonarr:latest` | 8989 (ev ağı + Tailscale) | 768m | unless-stopped |
| `stirling-pdf` | `stirling-pdf` | `frooodle/s-pdf:latest` | 8095 (ev ağı + Tailscale + internet (pdf.<alan-adı>, pdf.<alan-adı>)) | 1536m | unless-stopped |
| `subgen` | `subgen` | `mccloud/subgen:latest` | 8091 (ev ağı + Tailscale) | 4g | unless-stopped |
| `tapmap` | `tapmap-god-mode` | `{'context': 'https://github.com/olalie/tapmap.git#main', 'dockerfile': 'Dockerfile'}` | sunucu ağı (host) | 1G | unless-stopped |
| `tranga-api` | `tranga-api` | `glax/tranga-api:latest` | 6531 (ev ağı + Tailscale) | 768m | unless-stopped |
| `tranga-api` | `tranga-website` | `glax/tranga-website:latest` | 9555 (ev ağı + Tailscale) | 256m | unless-stopped |
| `tranga-api` | `tranga-pg` | `postgres:17` |  | 512m | unless-stopped |
| `transmission2` | `transmission` | `lscr.io/linuxserver/transmission:latest` |  | 768m | unless-stopped |
| `uptime-kuma` | `uptime-kuma` | `louislam/uptime-kuma:1` | 3004 (ev ağı + Tailscale + internet (status.<alan-adı>, status.<alan-adı>)) |  | unless-stopped |
| `webtop` | `webtop` | `lscr.io/linuxserver/webtop:ubuntu-kde` | 8101 (yalnız sunucu içi + internet (webtop.<alan-adı>)) | 3g | no |

## Ayrıntı

### `panel`

Dosya: `panel/compose.yaml`

- **homepage**: imaj `ghcr.io/gethomepage/homepage:latest`, portlar: 3010:3000, bellek sınırı: 384m
  - bağlı klasörler: `./homepage`, `./homepage/fontlar`, `/var/run/docker.sock`, `/mnt/side`, `/mnt/sidemain`
  - ortam değişkenleri: `HOMEPAGE_ALLOWED_HOSTS`

- **gundem-botu**: imaj `python:3.13-alpine`, portlar: 3011:8090, bellek sınırı: 128m
  - bağlı klasörler: `./gundem/gundem_botu.py`, `./gundem/veri`, `/home/flugel/sistem-bakim/durum`, `/var/lib/basket-bot`
  - ortam değişkenleri: `TZ`, `PYTHONDONTWRITEBYTECODE`

- **flugel-akis**: imaj `python:3.13-alpine`, portlar: 3012:8091, bellek sınırı: 512m
  - bağlı klasörler: `./akis/akis.py`, `./akis/web`, `./akis/veri`, `/var/lib/basket-bot`, `/home/flugel/sistem-bakim/durum`, `./homepage/services.yaml`
  - ortam değişkenleri: `TZ`, `PYTHONDONTWRITEBYTECODE`

### `adguard`

Dosya: `yiginlar/adguard/docker-compose.yml`

- **adguardhome**: imaj `adguard/adguardhome`, portlar: <IP>:53:53/tcp, <IP>:53:53/udp, <IP>:53:53/tcp, <IP>:53:53/udp, 0.0.0.0:3000:3000/tcp, 0.0.0.0:8888:80/tcp, 0.0.0.0:853:853/tcp, 0.0.0.0:853:853/udp, bellek sınırı: 768m
  - bağlı klasörler: `/home/flugel/adguard/work`, `/home/flugel/adguard/conf`, `/etc/letsencrypt`

### `ai-sandbox`

Dosya: `yiginlar/ai-sandbox/compose.yaml`

Yapay zeka kum havuzu: internet YOK (internal ag), salt-okunur, yetkisiz. Sadece ollama'ya erisir.

- **sohbet**: imaj `python:3.12-alpine`, bellek sınırı: 256m
  - bağlı klasörler: `./sohbet.py`, `/home/flugel/sistem-bakim/ai-sandbox`
  - ortam değişkenleri: `MODEL_A`, `MODEL_B`, `KONU`, `TUR`

### `bazarr`

Dosya: `yiginlar/bazarr/compose.yaml`

- **bazarr**: imaj `lscr.io/linuxserver/bazarr:latest`, portlar: 6767:6767, bellek sınırı: 1g
  - bağlı klasörler: `/arrapps/bazarr`, `/mnt/sidemain/movies`, `/mnt/sidemain/series`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`

### `code-server`

Dosya: `yiginlar/code-server/compose.yaml`

- **code-server**: imaj `lscr.io/linuxserver/code-server:latest`, portlar: 8444:8443, bellek sınırı: 1536m
  - bağlı klasörler: `/arrapps/code-server`, `/mnt/sidemain`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`, `PASSWORD`, `SUDO_PASSWORD`

### `convertx`

Dosya: `yiginlar/convertx/compose.yaml`

- **convertx**: imaj `ghcr.io/c4illin/convertx`, portlar: 3003:3000, bellek sınırı: 2g
  - bağlı klasörler: `/arrapps/convertx`
  - ortam değişkenleri: `JWT_SECRET`, `HTTP_ALLOWED`

### `daedalos`

Dosya: `yiginlar/daedalos/compose.yaml`

- **daedalos**: imaj `{'context': 'https://github.com/DustinBrett/daedalOS.git#main', 'dockerfile': 'Dockerfile'}`, portlar: 3005:3000, bellek sınırı: 1G

### `filebrowser`

Dosya: `yiginlar/filebrowser/compose.yaml`

- **filebrowser**: imaj `filebrowser/filebrowser:latest`, portlar: 8085:80
  - bağlı klasörler: `/`, `/DATA/AppData/filebrowser/database`, `/DATA/AppData/filebrowser/config`
  - ortam değişkenleri: `TZ`

### `flaresolverr`

Dosya: `yiginlar/flaresolverr/compose.yaml`

- **flaresolverr**: imaj `ghcr.io/flaresolverr/flaresolverr:latest`, ağ: container:gluetun, bellek sınırı: 1536m
  - ortam değişkenleri: `LOG_LEVEL`, `TZ`

### `giris`

Dosya: `yiginlar/giris/compose.yaml`

FLUGEL: <alan-adı> başlangıç sayfası + şifreli masaüstü anahtarı (/anahtar/). 127.0.0.1:8098 → Cloudflare tüneli

- **giris**: imaj `nginx:1.27-alpine`, portlar: 127.0.0.1:8098:80, bellek sınırı: 32m
  - bağlı klasörler: `./html`, `./nginx.conf`, `./htpasswd`

### `gluetun`

Dosya: `yiginlar/gluetun/docker-compose.yml`

- **gluetun**: imaj `qmcgaw/gluetun`, portlar: 8889:8888/tcp, 9091:9091/tcp, 51413:51413/tcp, 51413:51413/udp, 9696:9696/tcp, ağ: bridge, bellek sınırı: 256m
  - ortam değişkenleri: `VPN_SERVICE_PROVIDER`, `VPN_TYPE`, `WIREGUARD_PRIVATE_KEY`, `WIREGUARD_ADDRESSES`, `SERVER_COUNTRIES`, `BLOCK_IPV6`

### `gotify`

Dosya: `yiginlar/gotify/compose.yaml`

- **gotify**: imaj `gotify/server:latest`, portlar: 8482:80
  - bağlı klasörler: `/arrapps/gotify/data`
  - ortam değişkenleri: `GOTIFY_DEFAULTUSER_PASS`, `TZ`

### `immich_server`

Dosya: `yiginlar/immich_server/compose.yaml`

- **immich-server**: imaj `ghcr.io/immich-app/immich-server:release`, portlar: 2283:2283, bellek sınırı: 3g
  - bağlı klasörler: `/mnt/sidemain/immich`, `/etc/localtime`
  - ortam değişkenleri: `DB_HOSTNAME`, `DB_USERNAME`, `DB_PASSWORD`, `DB_DATABASE_NAME`, `REDIS_HOSTNAME`

- **immich-machine-learning**: imaj `ghcr.io/immich-app/immich-machine-learning:release-cuda`, bellek sınırı: 2g
  - bağlı klasörler: `/arrapps/immich/model-cache`
  - ortam değişkenleri: `DB_HOSTNAME`, `DB_USERNAME`, `DB_PASSWORD`, `DB_DATABASE_NAME`, `REDIS_HOSTNAME`, `IMMICH_TRITON_ENABLED`

- **redis**: imaj `docker.io/redis:6.2-alpine`, bellek sınırı: 256m

- **database**: imaj `ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0`, bellek sınırı: 1536m
  - bağlı klasörler: `/arrapps/immich/postgres`
  - ortam değişkenleri: `POSTGRES_PASSWORD`, `POSTGRES_USER`, `POSTGRES_DB`

### `it-tools`

Dosya: `yiginlar/it-tools/compose.yaml`

- **it-tools**: imaj `corentinth/it-tools:latest`, portlar: 8233:80, bellek sınırı: 256m

### `jackett`

Dosya: `yiginlar/jackett/compose.yaml`

- **jackett**: imaj `lscr.io/linuxserver/jackett:latest`, portlar: 9117:9117, bellek sınırı: 512m
  - bağlı klasörler: `/arrapps/jackett`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`, `AUTO_UPDATE`

### `kamiyomu`

Dosya: `yiginlar/kamiyomu/compose.yaml`

- **kamiyomu**: imaj `marcoscostadev/kamiyomu:latest`, portlar: 2342:8080, bellek sınırı: 1g
  - bağlı klasörler: `/etc/localtime`, `/mnt/sidemain/downloads/openbooks/books/kamiyomu`, `/mnt/sidemain/kamiyomu/database`, `/mnt/sidemain/kamiyomu/agents`, `/mnt/sidemain/kamiyomu/logs`
  - ortam değişkenleri: `TZ`

### `kasm`

Dosya: `yiginlar/kasm/compose.yaml`

FLUGEL: Kasm Workspaces — tarayıcıdan geçici sistemler (linuxserver/kasm, içinde Docker). 127.0.0.1:8103 → kasm.<alan-adı> İlk kurulum sihirbazı: ev ağından https://<sunucu-ip>:8102 (kendinden imzalı sertifika) (yönetici

- **kasm**: imaj `lscr.io/linuxserver/kasm:latest`, portlar: 8102:3000, 127.0.0.1:8103:443, ağ: bridge, ayrıcalıklı
  - bağlı klasörler: `./veri`, `./profiller`
  - ortam değişkenleri: `KASM_PORT`, `TZ`

### `kavita`

Dosya: `yiginlar/kavita/compose.yaml`

- **kavita**: imaj `lscr.io/linuxserver/kavita:latest`, portlar: 8295:5000, bellek sınırı: 768m
  - bağlı klasörler: `/arrapps/kavita`, `/mnt/sidemain/books`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`

### `komga`

Dosya: `yiginlar/komga/compose.yaml`

- **komga**: imaj `gotson/komga:latest`, portlar: 8296:25600, bellek sınırı: 1536m
  - bağlı klasörler: `/mnt/sidemain/books`, `/arrapps/komga`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`, `JAVA_OPTS`

### `libreoffice`

Dosya: `yiginlar/libreoffice/compose.yaml`

- **libreoffice**: imaj `lscr.io/linuxserver/libreoffice:latest`, portlar: 3205:3000, 3206:3001, bellek sınırı: 1536m
  - bağlı klasörler: `/opt/stacks/libreoffice/config`, `/mnt/sidemain`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`

### `lingarr`

Dosya: `yiginlar/lingarr/compose.yaml`

- **lingarr**: imaj `ghcr.io/lingarr-translate/lingarr:latest`, portlar: 5575:8080, bellek sınırı: 512m
  - bağlı klasörler: `/arrapps/lingarr`, `/mnt/sidemain/movies`, `/mnt/sidemain/series`
  - ortam değişkenleri: `TZ`, `DB_CONNECTION`

### `n8n`

Dosya: `yiginlar/n8n/compose.yaml`

- **n8n**: imaj `n8nio/n8n:latest`, portlar: 5678:5678, bellek sınırı: 1g
  - bağlı klasörler: `/arrapps/n8n`
  - ortam değişkenleri: `TZ`, `N8N_HOST`, `N8N_PORT`, `WEBHOOK_URL`, `N8N_SECURE_COOKIE`

### `netdata`

Dosya: `yiginlar/netdata/compose.yaml`

- **netdata**: imaj `netdata/netdata:latest`, portlar: 19999:19999, bellek sınırı: 768m
  - bağlı klasörler: `netdataconfig`, `netdatalib`, `netdatacache`, `/etc/passwd`, `/etc/group`, `/proc`, `/sys`, `/etc/os-release`, `/var/run/docker.sock`

### `nextcloud`

Dosya: `yiginlar/nextcloud/compose.yaml`

- **nextcloud**: imaj `lscr.io/linuxserver/nextcloud:latest`, portlar: 127.0.0.1:8443:443, <IP>:8443:443, bellek sınırı: 1536m
  - bağlı klasörler: `/arrapps/nextcloud`, `/mnt/sidemain/nextcloud_data`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`

### `openbooks`

Dosya: `yiginlar/openbooks/compose.yaml`

- **openbooks**: imaj `evanbuss/openbooks:latest`, portlar: 8285:80, bellek sınırı: 256m
  - bağlı klasörler: `/mnt/sidemain/books/ln`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`, `BASE_PATH`

### `prowlarr`

Dosya: `yiginlar/prowlarr/compose.yaml`

- **prowlarr**: imaj `lscr.io/linuxserver/prowlarr:latest`, ağ: container:gluetun, bellek sınırı: 512m
  - bağlı klasörler: `/arrapps/prowlarr`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`, `FLARESOLVERR_URL`

### `radarr`

Dosya: `yiginlar/radarr/compose.yaml`

- **radarr**: imaj `lscr.io/linuxserver/radarr:latest`, portlar: 7878:7878, bellek sınırı: 768m
  - bağlı klasörler: `/arrapps/radarr`, `/mnt/sidemain/movies`, `/mnt/side/downloads`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`

### `sonarr`

Dosya: `yiginlar/sonarr/compose.yaml`

- **sonarr**: imaj `lscr.io/linuxserver/sonarr:latest`, portlar: 8989:8989, bellek sınırı: 768m
  - bağlı klasörler: `/arrapps/sonarr`, `/mnt/sidemain/series`, `/mnt/side/downloads`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`

### `stirling-pdf`

Dosya: `yiginlar/stirling-pdf/compose.yaml`

- **stirling-pdf**: imaj `frooodle/s-pdf:latest`, portlar: 8095:8080, bellek sınırı: 1536m
  - bağlı klasörler: `/arrapps/stirling-pdf/trainingData`, `/arrapps/stirling-pdf/extraConfigs`, `/arrapps/stirling-pdf/customFiles`
  - ortam değişkenleri: `DOCKER_ENABLE_SECURITY`, `LANGS`

### `subgen`

Dosya: `yiginlar/subgen/compose.yaml`

- **subgen**: imaj `mccloud/subgen:latest`, portlar: 8091:9000, bellek sınırı: 4g
  - bağlı klasörler: `/mnt/sidemain/series`, `/mnt/sidemain/movies`
  - ortam değişkenleri: `WHISPER_MODEL`, `WHISPER_THREADS`, `CONCURRENT_TRANSCRIPTIONS`, `TRANSCRIBE_OR_TRANSLATE`, `NAMESUBLANG`, `OVERWRITE_EXISTINGSUBS`, `USE_GPU`, `TRANSCRIBE_DEVICE`, `PLEX_TOKEN`, `PLEX_SERVER`

### `tapmap`

Dosya: `yiginlar/tapmap/compose.yaml`

- **tapmap-god-mode**: imaj `{'context': 'https://github.com/olalie/tapmap.git#main', 'dockerfile': 'Dockerfile'}`, ağ: host, bellek sınırı: 1G, ayrıcalıklı
  - bağlı klasörler: `/DATA/AppData/tapmap/data`
  - ortam değişkenleri: `INTERFACE`

### `tranga-api`

Dosya: `yiginlar/tranga-api/compose.yaml`

- **tranga-api**: imaj `glax/tranga-api:latest`, portlar: 6531:6531, bellek sınırı: 768m
  - bağlı klasörler: `/mnt/sidemain/tranga/manga`, `/mnt/sidemain/tranga/settings`
  - ortam değişkenleri: `POSTGRES_HOST`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `TZ`

- **tranga-website**: imaj `glax/tranga-website:latest`, portlar: 9555:80, bellek sınırı: 256m

- **tranga-pg**: imaj `postgres:17`, bellek sınırı: 512m
  - bağlı klasörler: `tranga-pgdata`
  - ortam değişkenleri: `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`

### `transmission2`

Dosya: `yiginlar/transmission2/compose.yaml`

- **transmission**: imaj `lscr.io/linuxserver/transmission:latest`, ağ: container:gluetun, bellek sınırı: 768m
  - bağlı klasörler: `/arrapps/transmission`, `/mnt/side/downloads`, `/mnt/side/watch`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`

### `uptime-kuma`

Dosya: `yiginlar/uptime-kuma/compose.yaml`

- **uptime-kuma**: imaj `louislam/uptime-kuma:1`, portlar: 3004:3001
  - bağlı klasörler: `/arrapps/uptime-kuma`, `/var/run/docker.sock`

### `webtop`

Dosya: `yiginlar/webtop/compose.yaml`

FLUGEL: Webtop — tarayıcıdan kalıcı Ubuntu KDE masaüstü (linuxserver/webtop). 127.0.0.1:8101 → webtop.<alan-adı> Kasm ile aynı anda çalışmaz: flugel-webtop.service / flugel-kasm.service birbirini durdurur (restart: "no")

- **webtop**: imaj `lscr.io/linuxserver/webtop:ubuntu-kde`, portlar: 127.0.0.1:8101:3000, ağ: bridge, bellek sınırı: 3g
  - bağlı klasörler: `./config`
  - ortam değişkenleri: `PUID`, `PGID`, `TZ`, `TITLE`, `CUSTOM_USER`, `PASSWORD`, `LC_ALL`
