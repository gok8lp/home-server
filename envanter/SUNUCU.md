# Sunucu envanteri

Toplandı: 2026-10-17 13:33

## Sistem
```
  Static hostname: flugelserver
        Icon name: computer-desktop
          Chassis: desktop 🖥️
Chassis Asset Tag: To be filled by O.E.M.
 Operating System: Ubuntu 26.04.1 LTS
           Kernel: Linux 7.0.0-38-generic
     Architecture: x86-64
  Hardware Vendor: Micro-Star International Co., Ltd.
   Hardware Model: MS-7A38
 Hardware Version: 7.0
 Firmware Version: 9.E1
    Firmware Date: Sat 2022-07-16
     Firmware Age: 4y 3month 2d

CPU(s):                                  12
Model name:                              AMD Ryzen 5 2600X Six-Core Processor
               total        used        free      shared  buff/cache   available
Mem:            15Gi       7.5Gi       1.3Gi       562Mi       7.2Gi       7.6Gi
```

## Diskler
```
NAME                          SIZE TYPE  FSTYPE      MOUNTPOINTS
sda                         931.5G disk  crypto_LUKS 
└─sdd_crypt                 931.5G crypt ext4        /mnt/sidemain
sdb                         447.1G disk              
├─sdb1                          1G part  vfat        /boot/efi
├─sdb2                          2G part  ext4        /boot
└─sdb3                      444.1G part  crypto_LUKS 
  └─dm_crypt-0              444.1G crypt LVM2_member 
    └─ubuntu--vg-ubuntu--lv 444.1G lvm   ext4        /
sdc                         465.8G disk  crypto_LUKS 
└─sdc_crypt                 465.7G crypt ext4        /mnt/side

Filesystem                         Size  Used Avail Use% Mounted on
efivarfs                           128K   48K   76K  39% /sys/firmware/efi/efivars
/dev/mapper/ubuntu--vg-ubuntu--lv  437G  245G  173G  59% /
/dev/sdb2                          2.0G  247M  1.6G  14% /boot
/dev/sdb1                          1.1G  6.4M  1.1G   1% /boot/efi
/dev/mapper/sdc_crypt              458G  256G  180G  59% /mnt/side
/dev/mapper/sdd_crypt              916G  743G  127G  86% /mnt/sidemain
```

## Docker kapsayıcıları
```
NAMES                     IMAGE                                                            STATUS
kasm                      lscr.io/linuxserver/kasm:latest                                  Up
webtop                    lscr.io/linuxserver/webtop:ubuntu-kde                            Exited
giris                     nginx:1.27-alpine                                                Up
guacamole                 guacamole/guacamole:1.6.0                                        Up
guac-db                   postgres:16-alpine                                               Up
guacd                     guacamole/guacd:1.6.0                                            Up
uptime-kuma               louislam/uptime-kuma:1                                           Up
flugel-akis               python:3.13-alpine                                               Up
nextcloud                 lscr.io/linuxserver/nextcloud:latest                             Up
ollama                    ollama/ollama:latest                                             Up
plex                      lscr.io/linuxserver/plex:latest                                  Up
jellyfin                  lscr.io/linuxserver/jellyfin:latest                              Up
transmission              lscr.io/linuxserver/transmission:latest                          Up
prowlarr                  lscr.io/linuxserver/prowlarr:latest                              Up
flaresolverr              ghcr.io/flaresolverr/flaresolverr:latest                         Up
gluetun                   qmcgaw/gluetun                                                   Up
filebrowser               filebrowser/filebrowser:latest                                   Up
openbooks                 evanbuss/openbooks:latest                                        Up
immich_postgres           ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0   Up
immich_redis              redis:6.2-alpine                                                 Up
sonarr                    lscr.io/linuxserver/sonarr:latest                                Up
radarr                    lscr.io/linuxserver/radarr:latest                                Up
homepage                  ghcr.io/gethomepage/homepage:latest                              Up
netdata                   netdata/netdata:latest                                           Up
lingarr                   ghcr.io/lingarr-translate/lingarr:latest                         Up
komga                     gotson/komga:latest                                              Up
jackett                   lscr.io/linuxserver/jackett:latest                               Up
immich_server             ghcr.io/immich-app/immich-server:release                         Up
immich_machine_learning   ghcr.io/immich-app/immich-machine-learning:release-cuda          Up
code-server               lscr.io/linuxserver/code-server:latest                           Up
subgen                    mccloud/subgen:latest                                            Up
libreoffice               lscr.io/linuxserver/libreoffice:latest                           Up
gundem-botu               python:3.13-alpine                                               Up
stirling-pdf              frooodle/s-pdf:latest                                            Up
it-tools                  corentinth/it-tools:latest                                       Up
adguardhome               adguard/adguardhome                                              Up
open-webui                ghcr.io/open-webui/open-webui:main                               Up
portainer                 portainer/portainer-ce:latest                                    Up
kavita                    lscr.io/linuxserver/kavita:latest                                Up
bazarr                    lscr.io/linuxserver/bazarr:latest                                Up
tranga-website            glax/tranga-website:latest                                       Up
tranga-api                glax/tranga-api:latest                                           Up
tranga-pg                 postgres:17                                                      Up
convertx                  ghcr.io/c4illin/convertx                                         Up
kamiyomu                  marcoscostadev/kamiyomu:latest                                   Up
checkcle                  operacle/checkcle:latest                                         Up
dockge                    louislam/dockge:1                                                Up
```

## Sanal makineler
```
 Id   Name         State
-----------------------------
 10   mullvad-ts   running
 -    W11          shut off
 -    W11-GPU      shut off

```

## Etkin servisler (sunucuya özel)
```
flugel-uyari.path
boot-notify.service
cloudflared-akis.service
cloudflared.service
disk-apm.service
disk-keepalive.service
docker-guvenlik-duvari.service
docker.service
flugel-anahtar.service
gpu-manager.service
gpu-tasarruf.service
libvirtd.service
smbd.service
ssh-login-watcher.service
tailscaled.service
docker.socket
libvirtd-admin.socket
libvirtd-ro.socket
libvirtd.socket
ai-gozcu.timer
anime-takip.timer
basket-bot.timer
disk-health.timer
disk-koruyucu.timer
docker-watcher.timer
imdb-puan.timer
island-veri.timer
kritik-yedek.timer
morning-report.timer
self-heal.timer
swap-flush.timer
torrent-bekci.timer
virus-tarama.timer
weekly-maintenance.timer
```

## Zamanlayıcılar
```
ai-gozcu.service ai-gozcu.timer
anime-takip.service anime-takip.timer
apport-autoreport.service apport-autoreport.timer
apt-daily-upgrade.service apt-daily-upgrade.timer
apt-daily.service apt-daily.timer
basket-bot.service basket-bot.timer
certbot.service certbot.timer
chkrootkit.service chkrootkit.timer
disk-health.service disk-health.timer
disk-koruyucu.service disk-koruyucu.timer
docker-watcher.service docker-watcher.timer
dpkg-db-backup.service dpkg-db-backup.timer
e2scrub_all.service e2scrub_all.timer
fstrim.service fstrim.timer
imdb-puan.service imdb-puan.timer
island-veri.service island-veri.timer
kritik-yedek.service kritik-yedek.timer
logrotate.service logrotate.timer
morning-report.service morning-report.timer
motd-news.service motd-news.timer
phpsessionclean.service phpsessionclean.timer
pmie_check.service pmie_check.timer
pmie_daily.service pmie_daily.timer
pmie_farm_check.service pmie_farm_check.timer
pmlogger_check.service pmlogger_check.timer
pmlogger_daily.service pmlogger_daily.timer
pmlogger_farm_check.service pmlogger_farm_check.timer
pmproxy_check.service pmproxy_check.timer
pmproxy_daily.service pmproxy_daily.timer
self-heal.service self-heal.timer
snapd.snap-repair.service snapd.snap-repair.timer
swap-flush.service swap-flush.timer
sysstat-collect.service sysstat-collect.timer
sysstat-rotate.service sysstat-rotate.timer
sysstat-summary.service sysstat-summary.timer
systemd-tmpfiles-clean.service systemd-tmpfiles-clean.timer
torrent-bekci.service torrent-bekci.timer
virus-tarama.service virus-tarama.timer
weekly-maintenance.service weekly-maintenance.timer
xfs_scrub_all.service xfs_scrub_all.timer
```

## Elle kurulan paketler
```
acl apparmor apparmor-utils apport apt apt-transport-https bash bcache-tools bsdutils btrfs-progs 
build-essential ca-certificates certbot chkrootkit chrony clamav clamav-freshclam clevis clevis-initramfs 
clevis-luks clevis-systemd clevis-tpm2 cloud-init cloudflared cmake cockpit cockpit-bridge cockpit-packagekit 
cockpit-podman conntrack console-setup cpupower-gui cron crowdsec crowdsec-firewall-bouncer cryptsetup 
cryptsetup-initramfs cuda-toolkit curl dash dbus diffutils docker-compose-plugin docker.io dropbear-initramfs 
e2fsprogs earlyoom efibootmgr fail2ban fastfetch ffmpeg figlet findutils genisoimage gnupg grep 
grub-efi-amd64 grub-efi-amd64-signed gzip hd-idle hdparm hostname hwctl iotop iputils-ping kdump-tools 
libc-bin libguestfs-tools libvirt-dbus linux-crashdump linux-generic linux-tools-common linux-tools-generic 
lm-sensors locales lsof lvm2 lxd-installer mdadm mullvad-vpn multipath-tools nano ncdu ncurses-base 
ncurses-bin needrestart netbase nvidia-container-toolkit nvidia-driver-570 nvtop open-iscsi openssh-server 
pcp pcp-zeroconf php pollinate powertop python3-certbot-dns-cloudflare python3-openpyxl python3-pcp 
python3-pip python3.14-dev python3.14-venv rkhunter rsync samba samba-common-bin shim-signed smartmontools 
smbclient snapd speedtest-cli stress-ng sudo sysstat systemd systemd-resolved systemd-sysv tailscale 
tailscale-archive-keyring toilet tpm2-tools ubuntu-drivers-common ubuntu-release-upgrader-core udev ufw 
unattended-upgrades unminimize util-linux virtinst webmin wireguard wireguard-tools wsdd xfsprogs 
```
