INSTALLATION_COMMANDS = {
    # Web Browsers
    "Chromium": [
        "sudo zypper install -y chromium"
    ],
    "Google Chrome": [
        "sudo zypper addrepo https://dl.google.com/linux/chrome/rpm/stable/x86_64 google-chrome",
        "sudo zypper refresh",
        "sudo zypper install -y google-chrome-stable"
    ],
    "Vivaldi": [
        "sudo zypper addrepo https://repo.vivaldi.com/archive/vivaldi-suse.repo",
        "sudo zypper refresh",
        "sudo zypper install -y vivaldi-stable"
    ],
    "Opera": [
        "sudo zypper addrepo https://rpm.opera.com/rpm",
        "sudo zypper refresh",
        "sudo zypper install -y opera-stable"
    ],
    "Brave": [
        "sudo zypper addrepo https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo",
        "sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc",
        "sudo zypper refresh",
        "sudo zypper install -y brave-browser"
    ],

    # Development Tools
    "Git": [
        "sudo zypper install -y git"
    ],
    "Vim": [
        "sudo zypper install -y vim"
    ],
    "Emacs": [
        "sudo zypper install -y emacs"
    ],
    "Make": [
        "sudo zypper install -y make"
    ],
    "CMake": [
        "sudo zypper install -y cmake"
    ],
    "Python3 and Pip": [
        "sudo zypper install -y python3 python3-pip"
    ],

    # Networking Tools
    "Net-tools": [
        "sudo zypper install -y net-tools"
    ],
    "Traceroute": [
        "sudo zypper install -y traceroute"
    ],
    "Ping": [
        "sudo zypper install -y iputils"
    ],

    # IDEs
    "Visual Studio Code": [
        "sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc",
        "sudo zypper addrepo https://packages.microsoft.com/yumrepos/vscode vscode",
        "sudo zypper refresh",
        "sudo zypper install -y code"
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
        "sudo zypper install -y vlc"
    ],
    "mpv": [
        "sudo zypper install -y mpv"
    ],
    "Audacity": [
        "sudo zypper install -y audacity"
    ],
    "FFmpeg": [
        "sudo zypper install -y ffmpeg"
    ],

    # Terminals
    "Kitty": [
        "sudo zypper install -y kitty"
    ],
    "Alacritty": [
        "sudo zypper addrepo https://download.opensuse.org/repositories/home:/atim/alacritty/openSUSE_Tumbleweed/",
        "sudo zypper refresh",
        "sudo zypper install -y alacritty"
    ],

    # Graphics
    "Okular": [
        "sudo zypper install -y okular"
    ],
    "Scribus": [
        "sudo zypper install -y scribus"
    ],
    "GIMP": [
        "sudo zypper install -y gimp"
    ],
    "Inkscape": [
        "sudo zypper install -y inkscape"
    ],
    "Blender": [
        "sudo zypper install -y blender"
    ],
    "ImageMagick": [
        "sudo zypper install -y ImageMagick"
    ],

    # System Tools
    "Gparted": [
        "sudo zypper install -y gparted"
    ],
    "Disks": [
        "sudo zypper install -y gnome-disk-utility"
    ],
    "BleachBit": [
        "sudo zypper install -y bleachbit"
    ]
}