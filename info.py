DISTRO_FACTS = {
    "Ubuntu": """Ubuntu is the welcoming handshake into the world of Linux. Built on the sturdy foundation of Debian, it wraps everything in a user-friendly design that makes transitioning from Windows or macOS feel almost natural. Whether you’re setting up your first Linux system or deploying servers in the cloud, Ubuntu’s balance of usability and power makes it a versatile favorite.
    What makes it shine:
    - Uses APT and .deb packages for package management
    - Snap support allows for containerized apps with bundled dependencies
    - GNOME desktop offers a clean, modern interface
    - Long-Term Support (LTS) editions receive updates for 5 years
    - Extensive community and documentation for troubleshooting anything
Fun fact: Ubuntu means “humanity to others” in Zulu, which reflects its mission of making Linux accessible to everyone.
    """,

    "Debian": """If Linux distributions were skyscrapers, Debian would be the steel skeleton holding many of them upright. It’s one of the oldest, most trusted Linux bases out there. It values stability over flashiness, which is why it’s a go-to for servers and systems that need to just work — and keep working.
    What makes it dependable:
    - APT handles package management with .deb formats
    - Offers Stable, Testing, and Unstable branches — pick your level of risk
    - Runs on dozens of architectures from Raspberry Pi to enterprise servers
    - Highly focused on free software and strict testing of packages
    - Ideal for both serious server deployment and minimal desktop builds
Fun fact: Debian powers systems aboard the International Space Station. Now that’s stability you can trust.
    """,

    "Linux Mint": """Linux Mint is like Ubuntu’s friend who knows how to make everything more comfortable. It smooths out rough edges, adds useful features, and delivers a classic desktop experience. It’s perfect for new Linux users who want something reliable, beautiful, and easy to navigate.
    Why it’s user-friendly:
    - Uses APT and .deb but avoids Snap for more transparency
    - Supports multiple desktop environments: Cinnamon, MATE, XFCE
    - Flatpak integration for modern, secure app installation
    - Multimedia codecs are included right out of the box
    - Based on Ubuntu LTS for long-term stability with extra polish
Fun fact: The Cinnamon desktop was created by Mint’s developers to bring back a more traditional, Windows-like interface.
    """,

    "Pop!_OS": """Pop!_OS is Ubuntu’s stylish cousin — dressed for productivity and optimized for performance. Created by System76, it’s built to elevate creative work, programming, and gaming. With native support for NVIDIA and AMD drivers, it’s one of the most plug-and-play distros for modern hardware.
    What makes it a productivity powerhouse:
    - APT-based with Flatpak support, Snap optional
    - Uses a customized GNOME experience (COSMIC)
    - Comes with tiling window management for efficient multitasking
    - Great out-of-the-box support for GPUs, AI tools, and developer kits
    - Designed with creators, coders, and gamers in mind
Fun fact: Pop!_OS was one of the first distributions to install NVIDIA drivers automatically — no command line required.
    """,

    "Zorin OS": """Zorin OS feels like Linux dressed in a tailored suit. It’s sleek, beginner-focused, and customizable to feel like Windows or macOS — perfect for anyone making the switch. Beneath the elegant surface, you’ll find Ubuntu’s reliable engine.
    Why it's conversion-friendly:
    - Uses APT, supports Snap and Flatpak
    - Zorin Appearance tool lets you switch between UI layouts
    - Built-in Wine and PlayOnLinux support for running Windows apps
    - Offers a lightweight version for older PCs
    - Excellent fit for schools, home users, and visual perfectionists
Fun fact: Zorin OS was started by two teenage brothers in Ireland who believed Linux should be as approachable as any mainstream OS.
    """,

    "Fedora Workstation": """Fedora is where Linux goes to try new things. Sponsored by Red Hat, it’s fast-moving, developer-friendly, and often leads the way in adopting bleeding-edge features. If you want to stay current with Linux’s evolution while still enjoying a polished desktop, Fedora’s your playground.
    Why it’s forward-thinking:
    - Uses DNF for RPM-based package management
    - Ships with the newest GNOME releases and the Wayland display server
    - Flatpak is deeply integrated
    - New releases every 6 months, always up to date
    - Ideal for developers, creators, and Linux veterans
Fun fact: Fedora was the first major distro to switch to Wayland, replacing the decades-old X11 system.
    """,

    "Nobara": """Nobara is what happens when Fedora meets gaming. Built with content creators and gamers in mind, it removes the post-install hassle of setting up tools like OBS, Wine, and drivers — all the tweaks you’d normally have to Google are already done.
    Why gamers love it:
    - Based on Fedora, uses DNF and RPM
    - OBS Studio, Steam, Wine GE, and codecs come pre-installed
    - Game-ready kernel tweaks for performance
    - Optimized for streaming, emulation, and modding
    - Still has all of Fedora’s speed and tech under the hood
Fun fact: Nobara is developed by the creator of Proton GE, a major contributor to the Linux gaming revolution.
    """,

    "NixOS": """NixOS is the rule-breaker of the bunch. It treats system configuration like code — literally. Every detail, from installed packages to services, lives inside a configuration file. Want to rebuild or revert your system? One command does it. It’s automation-heavy, reproducible, and perfect for power users and DevOps lovers.
    What makes it unique:
    - Uses the Nix package manager with fully isolated builds
    - System state is declared in a single file
    - Atomic upgrades and rollbacks built into the core
    - Enables reproducible environments for development and deployment
    - Supports Linux containers, virtual machines, and more
Fun fact: In NixOS, even the kernel version can be rolled back with a single command. Mistakes are temporary.
    """,

    "openSUSE": """openSUSE gives you a choice: stability with Leap or bleeding-edge with Tumbleweed. It’s highly customizable, feature-rich, and known for its powerhouse tool YaST — a one-stop control center for managing your entire system.
    Why it’s versatile:
    - Uses Zypper and RPM packages
    - YaST offers GUI tools for network, partitioning, services, and more
    - Leap shares a codebase with SUSE Linux Enterprise, great for production
    - Tumbleweed is a tested rolling release for cutting-edge users
    - Built-in support for Btrfs snapshots and rollback
Fun fact: YaST is so robust, some sysadmins swear by it for managing large-scale enterprise environments.
    """,

    "Manjaro": """Manjaro makes the power of Arch Linux accessible to everyone. It provides the cutting-edge updates of Arch without the steep learning curve. This rolling release distro is optimized for performance and designed for ease of use.
    Why it's user-friendly:
    - User-friendly Arch: Simplifies Arch installation with a graphical installer
    - Hardware Detection: Auto-installs required drivers, including proprietary ones
    - Stable Rolling Release: Updates go through testing before being released
    - Multiple Desktop Environments: KDE, XFCE, GNOME editions available
    - Pamac Package Manager: Easy GUI-based software installation
Fun fact: Manjaro gives you the power of Arch with the usability of a beginner-friendly distro.
    """,

    "EndeavourOS": """EndeavourOS is like Arch Linux with a little hand-holding. It’s simple, minimal, and ideal for users who want the flexibility of Arch without the steep learning curve. A great starting point for Arch users who want to explore the full potential of the Arch ecosystem.
    Why it's Arch-like:
    - Close to Pure Arch: Simple, lightweight, and minimalistic
    - Community-Driven: Excellent support forums and Arch Wiki resources
    - Graphical Installer: No need for manual Arch setup (Calamares installer)
    - Rolling Release Model: Always up to date with the latest packages
    - Xfce Default, but Customizable: Choose your preferred DE after installation
Fun fact: EndeavourOS has one of the most helpful and vibrant communities in the Arch ecosystem.
    """,

    "Arch Linux": """Arch Linux is for Linux power users who want to craft their systems from the ground up. It’s minimal, lightweight, and doesn’t hold your hand — the installation process is entirely up to you. If you want total control over your system, Arch is the ultimate platform.
    Why it’s for power users:
    - Minimalist & Customizable: Install only what you need, no unnecessary bloatware
    - Rolling Release Model: Always up to date with the latest packages
    - Pacman Package Manager: Fast and efficient package management
    - AUR (Arch User Repository): Community-driven repository with thousands of extra packages
    - Arch Wiki: One of the best documentation resources in the Linux world
Fun fact: The Arch Wiki is so comprehensive that it’s often cited as a primary resource even by users of other Linux distros.
    """
}
