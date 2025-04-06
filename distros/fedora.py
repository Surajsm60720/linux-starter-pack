INSTALLATION_COMMANDS = {
    # Web Browsers
    "Chromium": [
        "sudo dnf install -y chromium"
    ],
    "Google Chrome": [
        "sudo dnf install -y fedora-workstation-repositories",
        "sudo dnf config-manager --set-enabled google-chrome",
        "sudo dnf install -y google-chrome-stable"
    ],
    "Vivaldi": [
        "sudo dnf config-manager --add-repo https://repo.vivaldi.com/archive/vivaldi-fedora.repo",
        "sudo dnf install -y vivaldi-stable"
    ],
    "Opera": [
        "sudo rpm --import https://rpm.opera.com/rpmrepo.key",
        "sudo dnf config-manager --add-repo https://rpm.opera.com/rpm",
        "sudo dnf install -y opera-stable"
    ],
    "Brave": [
        "sudo dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo",
        "sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc",
        "sudo dnf install -y brave-browser"
    ],

    # Development Tools
    "Git": [
        "sudo dnf install -y git"
    ],
    "Vim": [
        "sudo dnf install -y vim"
    ],
    "Emacs": [
        "sudo dnf install -y emacs"
    ],
    "Make": [
        "sudo dnf install -y make"
    ],
    "CMake": [
        "sudo dnf install -y cmake"
    ],
    "Python3 and Pip": [
        "sudo dnf install -y python3 python3-pip"
    ],

    # Networking Tools
    "Net-tools": [
        "sudo dnf install -y net-tools"
    ],
    "Traceroute": [
        "sudo dnf install -y traceroute"
    ],
    "Ping": [
        "sudo dnf install -y iputils"
    ],

    # IDEs
    "Visual Studio Code": [
        "sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc",
        "sudo sh -c 'echo -e \"[code]\\nname=Visual Studio Code\\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\\nenabled=1\\ngpgcheck=1\\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc\" > /etc/yum.repos.d/vscode.repo'",
        "sudo dnf install -y code"
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
        "sudo dnf install -y vlc"
    ],
    "mpv": [
        "sudo dnf install -y mpv"
    ],
    "Audacity": [
        "sudo dnf install -y audacity"
    ],
    "FFmpeg": [
        "sudo dnf install -y ffmpeg"
    ],

    # Terminals
    "Kitty": [
        "sudo dnf install -y kitty"
    ],
    "Alacritty": [
        "sudo dnf copr enable atim/alacritty -y",
        "sudo dnf install -y alacritty"
    ],

    # Graphics
    "Okular": [
        "sudo dnf install -y okular"
    ],
    "Scribus": [
        "sudo dnf install -y scribus"
    ],
    "GIMP": [
        "sudo dnf install -y gimp"
    ],
    "Inkscape": [
        "sudo dnf install -y inkscape"
    ],
    "Blender": [
        "sudo dnf install -y blender"
    ],
    "ImageMagick": [
        "sudo dnf install -y ImageMagick"
    ],

    # System Tools
    "Gparted": [
        "sudo dnf install -y gparted"
    ],
    "Disks": [
        "sudo dnf install -y gnome-disk-utility"
    ],
    "BleachBit": [
        "sudo dnf install -y bleachbit"
    ]
}