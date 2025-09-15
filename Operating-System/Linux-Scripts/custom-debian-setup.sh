#!/bin/bash

set -e

echo ">> Updating system..."
sudo apt update && sudo apt upgrade -y

# === Shell and Terminal Customization ===
echo ">> Installing Zsh and Oh My Zsh..."
sudo apt install -y zsh git curl
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# === Core Drivers and Networking Tools ===
echo ">> Installing drivers and networking utilities..."
sudo apt install -y \
  mesa-utils mesa-vulkan-drivers vulkan-tools \
  alsa-utils pulseaudio pipewire \
  network-manager network-manager-gnome \
  bluez blueman cups aircrack-ng kismet

# Enable services
sudo systemctl enable NetworkManager
sudo systemctl enable bluetooth
sudo systemctl enable cups

# === Package Managers ===
echo ">> Installing Flatpak, Snap, and Discover..."
sudo apt install -y flatpak snapd plasma-discover plasma-discover-backend-flatpak gparted partitionmanager

# Enable Snap and Flatpak
sudo snap install core
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# === Text Editors and Utilities ===
sudo apt install -y kate vim nano preload powertop timeshift

# === Security Tools ===
echo ">> Installing hardened kernel and security tools..."
sudo apt install -y \
  linux-image-amd64 \
  ufw gufw fail2ban apparmor apparmor-profiles apparmor-utils \
  tor i2p \
  auditd chkrootkit rkhunter clamav clamav-daemon \
  openvpn wireguard

# Enable services
sudo systemctl enable ufw
sudo systemctl enable fail2ban
sudo ufw enable

# === Development Tools ===
echo ">> Installing compilers and development packages..."
sudo apt install -y \
  build-essential gcc g++ make clang gdb \
  python3 python3-pip nodejs npm perl ruby \
  default-jdk rustc git gnuplot

# VS Code (via Microsoft repo)
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] \
https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install -y code
rm packages.microsoft.gpg

# === Multimedia Tools ===
sudo apt install -y vlc audacity obs-studio kde-spectacle

# === Browsers and Communication ===
sudo apt install -y firefox torbrowser-launcher discord

# Notion, WhatsApp (Snap or Flatpak)
sudo snap install notion-snap
sudo snap install whatsapp-for-linux

# === Office and Productivity ===
sudo apt install -y libreoffice playonlinux wine winetricks p7zip-full \
  gnuplot zotero todo.txt-cli gnome-weather nextcloud-desktop

# === Games ===
sudo apt install -y gbrainy tint tetrix pychess

# === Final Touch ===
echo ">> Enabling preload and powertop..."
sudo systemctl enable preload
sudo powertop --auto-tune

# === Change default shell to Zsh ===
chsh -s /bin/zsh

echo "✅ Setup complete! Please reboot your system."
