#!/bin/bash

# Exit on any error
set -e

# === Update system ===
echo ">> Updating system..."
sudo pacman -Syu --noconfirm

# === Install yay (AUR helper) ===
if ! command -v yay &> /dev/null; then
    echo ">> Installing yay (AUR helper)..."
    sudo pacman -S --needed base-devel git --noconfirm
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si --noconfirm
    cd ..
    rm -rf yay
fi


# === Terminal and Shell Customization ===
sudo pacman -S --noconfirm zsh oh-my-zsh zsh-syntax-highlighting zsh-autosuggestions

# === Core Drivers and Networking ===
sudo pacman -S --noconfirm mesa vulkan-radeon vulkan-intel vulkan-tools \
  alsa-utils pulseaudio pipewire pipewire-pulse \
  networkmanager network-manager-applet bluez blueman \
  aircrack-ng kismet cups

# Enable services
sudo systemctl enable NetworkManager
sudo systemctl enable bluetooth
sudo systemctl enable cups

# === Package Managers ===
sudo pacman -S --noconfirm flatpak snapd discover gparted partitionmanager

# Enable Snap & Flatpak
sudo ln -s /var/lib/snapd/snap /snap
sudo systemctl enable --now snapd.socket
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# === Text Editors & Dev Tools ===
sudo pacman -S --noconfirm kate vim nano timeshift preload powertop \
  base-devel gcc clang cmake gdb python python-pip nodejs npm rust perl ruby \
  openjdk11-openjdk git gnuplot jdk-openjdk

yay -S --noconfirm code

# === Security Tools ===
sudo pacman -S --noconfirm linux-hardened ufw gufw fail2ban apparmor \
  tor i2p audit auditctl chkrootkit rkhunter clamav openvpn wireguard-tools

# Enable firewalls and auditing
sudo systemctl enable ufw
sudo systemctl enable fail2ban
sudo ufw enable

# === Multimedia ===
sudo pacman -S --noconfirm vlc audacity obs-studio spectacle

# === Browsers and Communication ===
sudo pacman -S --noconfirm firefox torbrowser-launcher discord

yay -S --noconfirm whatsapp-for-linux notion-app-electron

# === Office & Utilities ===
sudo pacman -S --noconfirm libreoffice-still playonlinux wine winetricks \
  p7zip nextcloud-client todo.txt-cli zotero gnome-weather

# === Games ===
sudo pacman -S --noconfirm gbrainy tetris plymouth pychess

# === Final Touch ===
echo ">> Enabling preload & powertop optimizations..."
sudo systemctl enable preload
sudo systemctl enable powertop

# === Optional: Set zsh as default shell ===
chsh -s /bin/zsh

echo "✅ Setup complete! Please reboot your system."
