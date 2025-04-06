INSTALLATION_COMMANDS = {
    # Web Browsers
    "Chromium": [
        "nix-env -iA nixos.chromium"
    ],
    "Google Chrome": [
        "nix-env -iA nixos.google-chrome"
    ],
    "Vivaldi": [
        "nix-env -iA nixos.vivaldi"
    ],
    "Opera": [
        "nix-env -iA nixos.opera"
    ],
    "Brave": [
        "nix-env -iA nixos.brave"
    ],

    # Development Tools
    "Git": [
        "nix-env -iA nixos.git"
    ],
    "Vim": [
        "nix-env -iA nixos.vim"
    ],
    "Emacs": [
        "nix-env -iA nixos.emacs"
    ],
    "Make": [
        "nix-env -iA nixos.make"
    ],
    "CMake": [
        "nix-env -iA nixos.cmake"
    ],
    "Python3 and Pip": [
        "nix-env -iA nixos.python3 nixos.python3Packages.pip"
    ],

    # Networking Tools
    "Net-tools": [
        "nix-env -iA nixos.net-tools"
    ],
    "Traceroute": [
        "nix-env -iA nixos.traceroute"
    ],
    "Ping": [
        "nix-env -iA nixos.iputils"
    ],

    # IDEs
    "Visual Studio Code": [
        "nix-env -iA nixos.vscode"
    ],
    "PyCharm": [
        "nix-env -iA nixos.jetbrains.pycharm-community"
    ],
    "IntelliJ IDEA": [
        "nix-env -iA nixos.jetbrains.idea-community"
    ],
    "Eclipse": [
        "nix-env -iA nixos.eclipse"
    ],
    "Android Studio": [
        "nix-env -iA nixos.android-studio"
    ],
    "WebStorm": [
        "nix-env -iA nixos.jetbrains.webstorm"
    ],

    # Multimedia
    "Spotify": [
        "nix-env -iA nixos.spotify"
    ],
    "Discord": [
        "nix-env -iA nixos.discord"
    ],
    "VLC": [
        "nix-env -iA nixos.vlc"
    ],
    "mpv": [
        "nix-env -iA nixos.mpv"
    ],
    "Audacity": [
        "nix-env -iA nixos.audacity"
    ],
    "FFmpeg": [
        "nix-env -iA nixos.ffmpeg"
    ],

    # Terminals
    "Kitty": [
        "nix-env -iA nixos.kitty"
    ],
    "Alacritty": [
        "nix-env -iA nixos.alacritty"
    ],

    # Graphics
    "Okular": [
        "nix-env -iA nixos.okular"
    ],
    "Scribus": [
        "nix-env -iA nixos.scribus"
    ],
    "GIMP": [
        "nix-env -iA nixos.gimp"
    ],
    "Inkscape": [
        "nix-env -iA nixos.inkscape"
    ],
    "Blender": [
        "nix-env -iA nixos.blender"
    ],
    "ImageMagick": [
        "nix-env -iA nixos.imagemagick"
    ],

    # System Tools
    "Gparted": [
        "nix-env -iA nixos.gparted"
    ],
    "Disks": [
        "nix-env -iA nixos.gnome-disk-utility"
    ],
    "BleachBit": [
        "nix-env -iA nixos.bleachbit"
    ]
}