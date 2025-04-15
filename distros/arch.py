INSTALLATION_COMMANDS = {
    # Web Browsers
    "Chromium": [
        "sudo pacman -S --noconfirm chromium"
    ],
    "Google Chrome": [
        "git clone https://aur.archlinux.org/google-chrome.git",
        "cd google-chrome/",
        "makepkg -s",
        "sudo pacman -U --noconfirm google-chrome-*.xz"
    ],
    "Vivaldi": [
        "yay -S --noconfirm vivaldi"
    ],
    "Opera": [
        "sudo pacman -S opera"
    ],
    "Brave": [
        "yay -Sy brave-bin"
    ],

    # Development Tools
    "Git": [
        "sudo pacman -S --noconfirm git"
    ],
    "Vim": [
        "sudo pacman -S --noconfirm vim"
    ],
    "Emacs": [
        "sudo pacman -S --noconfirm emacs"
    ],
    "Make": [
        "sudo pacman -S --noconfirm make"
    ],
    "CMake": [
        "sudo pacman -S --noconfirm cmake"
    ],
    "Python3 and Pip": [
        "sudo pacman -S --noconfirm python python-pip"
    ],

    # Networking Tools
    "Net-tools": [
        "sudo pacman -S --noconfirm net-tools"
    ],
    "Traceroute": [
        "sudo pacman -S --noconfirm traceroute"
    ],
    "Ping": [
        "sudo pacman -S --noconfirm iputils"
    ],

    # IDEs
    "Visual Studio Code": [
        "yay -S --noconfirm visual-studio-code-bin"
    ],
    "PyCharm": [
        "sudo pacman -S --noconfirm pycharm-community-edition"
    ],
    "IntelliJ IDEA": [
        "sudo pacman -S --noconfirm intellij-idea-community-edition"
    ],
    "Eclipse": [
        "sudo pacman -S --noconfirm eclipse-java"
    ],
    "Android Studio": [
        "yay -S --noconfirm android-studio"
    ],
    "WebStorm": [
        "yay -S --noconfirm webstorm"
    ],

    # Multimedia
    "Spotify": [
        "yay -S --noconfirm spotify"
    ],
    "Discord": [
        "sudo pacman -S --noconfirm discord"
    ],
    "VLC": [
        "sudo pacman -S --noconfirm vlc"
    ],
    "mpv": [
        "sudo pacman -S --noconfirm mpv"
    ],
    "Audacity": [
        "sudo pacman -S --noconfirm audacity"
    ],
    "FFmpeg": [
        "sudo pacman -S --noconfirm ffmpeg"
    ],

    # Terminals
    "Kitty": [
        "sudo pacman -S --noconfirm kitty"
    ],
    "Alacritty": [
        "sudo pacman -S --noconfirm alacritty"
    ],

    # Graphics
    "Okular": [
        "sudo pacman -S --noconfirm okular"
    ],
    "Scribus": [
        "sudo pacman -S --noconfirm scribus"
    ],
    "GIMP": [
        "sudo pacman -S --noconfirm gimp"
    ],
    "Inkscape": [
        "sudo pacman -S --noconfirm inkscape"
    ],
    "Blender": [
        "sudo pacman -S --noconfirm blender"
    ],
    "ImageMagick": [
        "sudo pacman -S --noconfirm imagemagick"
    ],

    # System Tools
    "Gparted": [
        "sudo pacman -S --noconfirm gparted"
    ],
    "Disks": [
        "sudo pacman -S --noconfirm gnome-disk-utility"
    ],
    "BleachBit": [
        "sudo pacman -S --noconfirm bleachbit"
    ]
}