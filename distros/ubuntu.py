INSTALLATION_COMMANDS = {
    # Web Browsers
    "Chromium": [
        "sudo apt install -y chromium-browser"
    ],
    "Google Chrome": [
        "wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -",
        "echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list",
        "sudo apt update",
        "sudo apt install -y google-chrome-stable"
    ],
    "Vivaldi": [
        "wget -qO- https://repo.vivaldi.com/archive/linux_signing_key.pub | sudo apt-key add -",
        "echo 'deb [arch=amd64] https://repo.vivaldi.com/archive/deb/ stable main' | sudo tee /etc/apt/sources.list.d/vivaldi.list",
        "sudo apt update",
        "sudo apt install -y vivaldi-stable"
    ],
    "Opera": [
        "wget -qO- https://deb.opera.com/archive.key | sudo apt-key add -",
        "echo 'deb [arch=amd64] https://deb.opera.com/opera-stable/ stable non-free' | sudo tee /etc/apt/sources.list.d/opera-stable.list",
        "sudo apt update",
        "sudo apt install -y opera-stable"
    ],
    "Brave": [
        "sudo apt install -y curl",
        "curl -fsSL https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo tee /usr/share/keyrings/brave-browser-archive-keyring.gpg > /dev/null",
        "echo 'deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main' | sudo tee /etc/apt/sources.list.d/brave-browser-release.list",
        "sudo apt update",
        "sudo apt install -y brave-browser"
    ],
    # Development Tools
    "Git": [
        "sudo apt install -y git"
    ],
    "Vim": [
        "sudo apt install -y vim"
    ],
    "Emacs": [
        "sudo apt install -y emacs"
    ],
    "Make": [
        "sudo apt install -y make"
    ],
    "CMake": [
        "sudo apt install -y cmake"
    ],
    "Python3 and Pip": [
        "sudo apt install -y python3 python3-pip"
    ],

    # Networking Tools
    "Curl": [
        "sudo apt install -y curl"
    ],
    "Wget": [
        "sudo apt install -y wget"
    ],
    "Net-tools": [
        "sudo apt install -y net-tools"
    ],
    "Traceroute": [
        "sudo apt install -y traceroute"
    ],
    "Ping": [
        "sudo apt install -y iputils-ping"
    ],

    # IDEs
    "Visual Studio Code": [
        "wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /usr/share/keyrings/packages.microsoft.gpg > /dev/null",
        "echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main' | sudo tee /etc/apt/sources.list.d/vscode.list",
        "sudo apt update",
        "sudo apt install -y code"
    ],
    "PyCharm": [
        "sudo snap install pycharm-community --classic"
    ],
    "IntelliJ IDEA": [
        "sudo snap install intellij-idea-community --classic"
    ],
    "Eclipse": [
        "sudo snap install eclipse --classic"
    ],
    "Android Studio": [
        "sudo snap install android-studio --classic"
    ],
    "WebStorm": [
        "sudo snap install webstorm --classic"
    ],

    # Multimedia
    "Spotify": [
        "sudo snap install spotify"
    ],
    "Discord": [
        "sudo snap install discord"
    ],
    "VLC": [
        "sudo apt install -y vlc"
    ],
    "mpv": [
        "sudo apt install -y mpv"
    ],
    "Audacity": [
        "sudo apt install -y audacity"
    ],
    "FFmpeg": [
        "sudo apt install -y ffmpeg"
    ],

    # Terminals
    "Kitty": [
        "sudo apt install -y kitty"
    ],
    "Alacritty": [
        "sudo add-apt-repository ppa:aslatter/ppa -y",
        "sudo apt update",
        "sudo apt install -y alacritty"
    ],

    # Graphics
    "Okular": [
        "sudo apt install -y okular"
    ],
    "Scribus": [
        "sudo apt install -y scribus"
    ],
    "GIMP": [
        "sudo apt install -y gimp"
    ],
    "Inkscape": [
        "sudo apt install -y inkscape"
    ],
    "Blender": [
        "sudo apt install -y blender"
    ],
    "ImageMagick": [
        "sudo apt install -y imagemagick"
    ],

    # System Tools
    "Gparted": [
        "sudo apt install -y gparted"
    ],
    "Disks": [
        "sudo apt install -y gnome-disk-utility"
    ],
    "BleachBit": [
        "sudo apt install -y bleachbit"
    ]
}
