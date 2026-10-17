# Sanal makineler

libvirt/KVM; tanımlar [`libvirt/vm/`](../libvirt/vm/), donanım tablosu [otomatik/SANAL-MAKINELER.md](otomatik/SANAL-MAKINELER.md).

## W11-GPU ve W11 (Windows 11)

- Aynı disk; W11-GPU ekran kartını (GTX 1660 Ti) doğrudan alır, W11 GPU'suzdur.
- **GPU geçirme:** [`libvirt/qemu-hook`](../libvirt/qemu-hook) W11-GPU açılırken kartı NVIDIA sürücüsünden ayırıp
  `vfio-pci`'ye bağlar (`bin/gpu-to-vm.sh`), kapanınca sunucuya geri verir (`bin/gpu-to-host.sh`). Kart sanal
  makinedeyken GPU kullanan kapsayıcılar (Ollama, Whisper altyazı) bilerek durdurulur; izleyiciler bunu sorun saymaz.
  Kanca yalnız bu PCI veri yolu için çalışacak şekilde yazılmıştır.
- **Akış:** Apollo (sanal makinede) + Moonlight (PC/telefon); portlar `sbin/vm-yonlendir.sh` ile sunucudan yönlendirilir.
- Bellek küçük olduğu için sanal makine açmadan önce boş bellek hesaplanır. Çalışırken disk/ISO değiştirmek
  (`virsh change-media`) QEMU'yu kilitlediği için yapılmaz. Sanal makineler zorla kapatılmaz (`virsh destroy` yok).

## mullvad-ts (Ubuntu 24.04): VPN + geliştirme masaüstü

- **VPN:** Mullvad + Tailscale çıkış düğümü olarak tasarlandı (Mullvad bağlantısı hesap girişi gerektirir).
- **Masaüstü:** 4 sanal çekirdek, 4 GB RAM, 30 GB disk; XFCE, Ubuntu görünümünde (Yaru karanlık, solda dock, üstte
  saat), ekran birleştirici kapalı; Eclipse, gcc/gdb/cmake/clang/valgrind, Java, Python. Ayarlar:
  [`vm/mullvad-ts/`](../vm/mullvad-ts/), düzen betiği `root/xfce-ubuntu.py`.
- **Kalıcılık:** sunucuyla birlikte açılır (`autostart`), statik IP, açılış ~27 sn (ağ beklemesi kısaltıldı),
  giriş ekranı garantili başlar (`flugel-ekran.service`). Elle kapatıp açınca her şey aynı gelir.
- **Eşitleme:** Syncthing ile PC'deki `eclipse-workspace` klasörü iki yönlü; Eclipse'in `.metadata` klasörü her
  makinede ayrı (iki Eclipse aynı anda açıkken çakışmasın).
- **Root işleri şifresiz:** sunucuda `bakim/vmroot.sh 'komut'` (qemu-guest-agent `guest-exec`).
- Erişim ve oturum davranışı: [UZAK-MASAUSTU.md](UZAK-MASAUSTU.md).
