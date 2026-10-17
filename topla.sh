#!/bin/bash
# home-server: ev sunucusunun tamamını depoya toplar ve temizler.
#   sistem/     /etc altındaki sistem ayarları (ağ, depolama, Samba, SSH, güvenlik duvarı, GRUB/VFIO, cron, udev…)
#   yiginlar/   /opt/stacks/* Docker yığınları (compose + küçük yapılandırma dosyaları; .env/veri yok)
#   panel/, basket-bot/, scripts/   FLUGEL paneli + Akış, botlar, Gmail bildirici
#   systemd/, bin/, sbin/, lib/, bakim/   servisler ve betikler
#   cloudflared/, libvirt/   tüneller, GPU kancası, sanal makine tanımları ve ağları
#   vm/mullvad-ts/   geliştirme masaüstü sanal makinesinin sistem ayarları ve betikleri
#   envanter/   anlık donanım/yazılım envanteri (her toplamada yenilenir)
# Gizli/kişisel bilgiler temizle.py ile çıkarılır; kişisel değerler depo dışındaki ~/.config/flugel-depo/gizli.txt'te.
set -e
R="$(cd "$(dirname "$0")" && pwd)"; S=$(mktemp -d); trap 'rm -rf "$S"' EXIT
GIZLI="$HOME/.config/flugel-depo/gizli.txt"

ssh flugelserver 'cd / && sudo tar czf - --exclude=__pycache__ --exclude="*.bak" --exclude="*.onceki*" --exclude=".env*" --exclude=htpasswd \
 $(cd /opt/stacks && for d in */; do find "$d" -maxdepth 1 -type f \( -name "*.yml" -o -name "*.yaml" -o -name "*.conf" -o -name "*.py" -o -name "*.sh" -o -name "*.toml" -o -name "*.json" \) -size -200k; done | sed "s|^|opt/stacks/|") \
 opt/stacks/docker-compose.yml opt/stacks/giris/html opt/stacks/guacamole/initdb/02-flugel.sql \
 opt/stacks/panel/homepage/settings.yaml opt/stacks/panel/homepage/services.yaml opt/stacks/panel/homepage/widgets.yaml opt/stacks/panel/homepage/bookmarks.yaml opt/stacks/panel/homepage/docker.yaml \
 opt/stacks/panel/homepage/custom.css opt/stacks/panel/homepage/custom.js opt/stacks/panel/gundem/gundem_botu.py opt/stacks/panel/akis/akis.py opt/stacks/panel/akis/web \
 opt/basket-bot/basket_bot.py opt/basket-bot/anime_takip.py opt/basket-bot/imdb_puan.py opt/basket-bot/ayar.json opt/scripts \
 etc/cloudflared/akis.yml etc/cloudflared/config.yml etc/libvirt/hooks/qemu etc/libvirt/qemu/networks/default.xml \
 $(cd /etc/libvirt/qemu && ls *.xml | sed "s|^|etc/libvirt/qemu/|") \
 etc/samba/smb.conf etc/smartd.conf etc/docker/daemon.json etc/fstab etc/crypttab etc/hosts etc/default/grub etc/default/hd-idle \
 etc/ssh/sshd_config etc/ssh/sshd_config.d etc/ufw/user.rules etc/ufw/user6.rules etc/crontab etc/cron.d etc/netplan etc/sysctl.d \
 etc/modprobe.d/vfio.conf etc/modprobe.d/blacklist-nvidia.conf etc/modprobe.d/disable-ucsi.conf etc/udev/rules.d \
 etc/systemd/logind.conf.d etc/systemd/journald.conf.d etc/apache2/sites-enabled \
 $(cd /etc/systemd/system && ls | grep -E "\.(service|timer|path)$" | grep -vE "^(dbus|sshd|snap|syslog|cloud-|getty|display-manager|systemd-|chronyd|nmb|smb|smartd|wsdd|nvidia-persistenced)" | sed "s|^|etc/systemd/system/|") \
 $(cd /usr/local/bin && ls | grep -E "\.sh$|^(ai-sohbet|bildirim|emoji-sembol|telegram-kur)$" | sed "s|^|usr/local/bin/|") \
 $(cd /usr/local/sbin && ls | grep -E "\.(sh|py)$" | sed "s|^|usr/local/sbin/|") usr/local/lib/sistem-bakim \
 $(cd /home/flugel/sistem-bakim && ls *.sh *.py 2>/dev/null | sed "s|^|home/flugel/sistem-bakim/|") 2>/dev/null' | tar xzf - -C "$S"

# envanter (anlık)
mkdir -p "$S/envanter"
ssh flugelserver 'echo "# Sunucu envanteri"; echo; echo "Toplandı: $(date "+%F %H:%M")"; echo; echo "## Sistem"; echo "\`\`\`"; hostnamectl | grep -vE "Machine ID|Boot ID"; echo; lscpu | grep -E "Model name|^CPU\(s\)"; free -h | head -2; echo "\`\`\`"; \
 echo; echo "## Diskler"; echo "\`\`\`"; lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS -e7; echo; df -h -x tmpfs -x devtmpfs -x overlay -x squashfs; echo "\`\`\`"; \
 echo; echo "## Docker kapsayıcıları"; echo "\`\`\`"; docker ps -a --format "table {{.Names}}\t{{.Image}}\t{{.Status}}" | sed -E "s/Up [^\t]*/Up/; s/Exited [^\t]*/Exited/"; echo "\`\`\`"; \
 echo; echo "## Sanal makineler"; echo "\`\`\`"; sudo virsh list --all; echo "\`\`\`"; \
 echo; echo "## Etkin servisler (sunucuya özel)"; echo "\`\`\`"; systemctl list-unit-files --state=enabled --no-legend | awk "{print \$1}" | grep -E "^(flugel|cloudflared|ai-|anime|basket|boot|disk|docker|imdb|island|kritik|morning|self|ssh-login|swap|torrent|virus|weekly|gpu|hd-idle|smartd|smb|tailscaled|libvirtd)" ; echo "\`\`\`"; \
 echo; echo "## Zamanlayıcılar"; echo "\`\`\`"; systemctl list-timers --all --no-legend | awk "{print \$NF, \$(NF-1)}" | grep -v "^$" | sort -u | head -60; echo "\`\`\`"; \
 echo; echo "## Elle kurulan paketler"; echo "\`\`\`"; apt-mark showmanual | tr "\n" " " | fold -s -w 110; echo; echo "\`\`\`"' > "$S/envanter/SUNUCU.md"

# mullvad-ts sanal makinesi
mkdir -p "$S/vm"
ssh flugelserver '~/sistem-bakim/vmroot.sh "cd / && tar czf - usr/local/bin/flugel-bosta.sh usr/local/bin/flugel-tek-oturum.sh etc/systemd/system/flugel-bosta.service etc/systemd/system/flugel-bosta.timer etc/systemd/system/flugel-ekran.service etc/systemd/system/systemd-networkd-wait-online.service.d etc/netplan etc/cloud/cloud.cfg.d/99-flugel-ag.cfg etc/xrdp/xrdp.ini etc/lightdm/lightdm.conf.d etc/polkit-1/rules.d/45-flugel-xrdp.rules etc/pam.d/xrdp-sesman etc/pam.d/lightdm etc/dconf/db/local.d etc/dconf/profile/user root/xfce-ubuntu.py root/xfce-duzelt.py root/sade.sh root/gnome-kur.sh 2>/dev/null | base64 -w0"' | base64 -d | tar xzf - -C "$S/vm" 2>/dev/null || true

# depo düzeni
for k in sistem yiginlar panel basket-bot scripts systemd bin sbin lib bakim cloudflared libvirt vm envanter; do rm -rf "$R/$k"; done
mkdir -p "$R"/{sistem,yiginlar,panel,basket-bot,scripts,systemd,bin,sbin,lib,bakim,cloudflared,libvirt/vm,vm/mullvad-ts,envanter}
cp -r "$S"/etc/. "$R/sistem/"; rm -rf "$R/sistem/systemd/system" "$R/sistem/cloudflared" "$R/sistem/libvirt"
cp -r "$S"/opt/stacks/. "$R/yiginlar/"; mv "$R/yiginlar/panel"/* "$R/panel/" 2>/dev/null || true; rm -rf "$R/yiginlar/panel"
mv "$R/yiginlar/docker-compose.yml" "$R/yiginlar/_ana-docker-compose.yml"
cp "$S"/opt/basket-bot/* "$R/basket-bot/"; cp -r "$S"/opt/scripts/. "$R/scripts/"
cp "$S"/etc/systemd/system/* "$R/systemd/"; cp "$S"/usr/local/bin/* "$R/bin/"; cp "$S"/usr/local/sbin/* "$R/sbin/"
cp -r "$S"/usr/local/lib/sistem-bakim/. "$R/lib/"; cp "$S"/home/flugel/sistem-bakim/* "$R/bakim/"
cp "$S"/etc/cloudflared/*.yml "$R/cloudflared/"; cp "$S"/etc/libvirt/hooks/qemu "$R/libvirt/qemu-hook"
cp "$S"/etc/libvirt/qemu/*.xml "$R/libvirt/vm/"; cp "$S"/etc/libvirt/qemu/networks/default.xml "$R/libvirt/ag-default.xml"
cp -r "$S"/vm/. "$R/vm/mullvad-ts/" 2>/dev/null || true; cp "$S"/envanter/* "$R/envanter/"

# temizlik
python3 "$R/temizle.py" "$R" "$GIZLI"; mv "$R/.env.ornek" "$R/env.ornek"
sed -i 's/>[^<]*<\/h1>/>FLUGEL<\/h1>/; s/<title>[^<]*<\/title>/<title>FLUGEL<\/title>/' "$R/yiginlar/giris/html/index.html"
sed -i -E 's/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/<kimlik>/g' "$R"/cloudflared/*.yml
echo "toplandı: $(find "$R" -type f -not -path "*/.git/*" | wc -l) dosya"
