#!/bin/bash

set -e

echo ">> Updating Fedora system..."
sudo dnf update -y

# === Enable RPM Fusion Repos ===
echo ">> Enabling RPM Fusion..."
sudo dnf install -y \
  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
  https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

# === Shell: Zsh + Oh My Zsh ===
echo ">> Installing Zsh and Oh My Zsh..."
sudo dnf install -y zsh git curl util-linux-user
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# === Core Drivers and Utilities ===
sudo dnf install -y \
  mesa-dri-drivers vulkan vulkan-tools \
  alsa-utils pulseaudio pipewire wireplumber \
  NetworkManager NetworkManager-wifi NetworkManager-bluetooth \
  bluez blueman cups aircrack-ng kismet

# Enable essential services
sudo systemctl enable NetworkManager
sudo systemctl enable bluetooth
sudo systemctl enable cups

# === Package Managers & Disk Tools ===
sudo dnf install -y flatpak gnome-software gnome-software-plugin-flatpak \
  gparted kde-partitionmanager

# Add Flathub
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# === Editors & Utilities ===
sudo dnf install -y kate vim nano preload powertop timeshift

# === Security Tools ===
sudo dnf install -y \
  kernel-core kernel-devel \
  ufw gufw fail2ban apparmor \
  tor i2p \
  audit audit-libs auditd chkrootkit rkhunter \
  clamav clamav-update openvpn wireguard-tools

# Enable services
sudo systemctl enable ufw
sudo systemctl enable fail2ban
sudo ufw enable

# === Development Tools ===
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y \
  gcc gcc-c++ make clang gdb cmake \
  python3 python3-pip nodejs npm ruby perl \
  java-11-openjdk rust git gnuplot

# Install VS Code (via Microsoft repo)
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
sudo dnf check-update
sudo dnf install -y code

# === Multimedia ===
sudo dnf install -y vlc audacity obs-studio kde-spectacle

# === Browsers & Communication ===
sudo dnf install -y firefox torbrowser-launcher discord

# === Snap Support for Notion/WhatsApp ===
sudo dnf install -y snapd
sudo ln -s /var/lib/snapd/snap /snap
sudo systemctl enable --now snapd.socket
sudo snap install notion-snap
sudo snap install whatsapp-for-linux

# === Office and Cloud Tools ===
sudo dnf install -y libreoffice playonlinux wine p7zip p7zip-plugins \
  nextcloud-client todo.txt gnuplot gnome-weather

# Zotero (Flatpak)
flatpak install -y flathub org.zotero.Zotero

# === Games ===
sudo dnf install -y gbrainy pychess

# === Final Touch ===
echo ">> Enabling preload and powertop optimization..."
sudo systemctl enable preload
sudo powertop --auto-tune

# === Change default shell to Zsh ===
chsh -s $(which zsh)

echo "✅ Fedora setup complete! Please reboot your system."
