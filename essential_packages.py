commands = {
"Ubuntu": """
    sudo apt update
    sudo apt install -y curl wget snapd
    sudo systemctl enable --now snapd.socket
""",
"Debian": """
    sudo apt update
    sudo apt install -y curl wget snapd
    sudo systemctl enable --now snapd.socket
""",
"Linux Mint": """
    sudo apt update
    sudo apt install snapd
    sudo apt install -y curl wget
""",
"Pop!_OS": """
    sudo apt update
    sudo apt install -y curl wget snapd
    sudo systemctl enable --now snapd.socket
""",
"Zorin OS": """
    sudo apt update
    sudo apt install -y curl wget snapd
    sudo systemctl enable --now snapd.socket
""",
"Fedora Workstation": """
    sudo dnf update -y
    sudo dnf install -y curl wget snapd
    sudo systemctl enable --now snapd.socket
""",
"Nobara": """
    sudo dnf update -y
    sudo dnf install -y curl wget snapd
    sudo systemctl enable --now snapd.socket
""",
"openSUSE": """
    sudo zypper refresh
    sudo zypper addrepo --refresh \
        https://download.opensuse.org/repositories/system:/snappy/openSUSE_Tumbleweed \
            snappy
    sudo zypper --gpg-auto-import-keys refresh
    sudo zypper dup --from snappy
    sudo zypper install -y curl wget snapd
    sudo systemctl enable --now snapd.socket
    sudo systemctl enable --now snapd.apparmor
""",
"Manjaro": """
    sudo pacman -Syu --noconfirm
    sudo pacman -S --noconfirm curl wget snapd
    sudo systemctl enable --now snapd.socket
    sudo ln -s /var/lib/snapd/snap /snap
""",
"EndeavourOS": """
    sudo pacman -Syu --noconfirm
    sudo pacman -S --noconfirm curl wget snapd  
    sudo systemctl enable --now snapd.socket
    sudo ln -s /var/lib/snapd/snap /snap
""",
"Arch Linux": """
    sudo pacman -Syu --noconfirm
    git clone https://aur.archlinux.org/snapd.git
    cd snapd
    makepkg -si
    sudo systemctl enable --now snapd.socket
    sudo ln -s /var/lib/snapd/snap /snap
    sudo pacman -S --noconfirm curl wget
""",
"NixOS": """
    nix-env -iA wget curl
""",
        }