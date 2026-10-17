#!/bin/bash
# Depoyu sunucunun güncel hâliyle yeniler, gizli bilgi taraması yapar, commit'ler ve GitHub'a gönderir.
# Kullanım: ./guncelle.sh "açıklama"
set -e
cd "$(dirname "$0")"
./topla.sh
GIZLI="$HOME/.config/flugel-depo/gizli.txt"
if grep -rnIF --exclude-dir=.git --exclude=temizle.py --exclude=topla.sh -f <(cut -f1 "$GIZLI") . \
   || grep -rnIE --exclude-dir=.git "[0-9]{8,10}:[A-Za-z0-9_-]{30,}|BEGIN [A-Z ]*PRIVATE KEY|gh[op]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}" . ; then
  echo "!!! Gizli bilgi bulundu, gönderilmedi."; exit 1
fi
git add -A
git diff --cached --quiet && { echo "Değişiklik yok."; exit 0; }
git commit -q -m "${1:-Güncelleme $(date '+%F %H:%M')}"
git push -q origin main && echo "Gönderildi: $(git log -1 --format='%h %s')"
