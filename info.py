DISTRO_FACTS = {
    "Ubuntu": """
    - User-friendly: Ideal for beginners with a polished UI and simple installation.
    - LTS Releases: Long-term support versions with 5 years of updates.
    - Extensive Software Support: Large repository with Snap, Flatpak, and AppImage support.
    - Strong Community Support: Active forums, tutorials, and vast documentation.
    - Cloud & Server Optimization: Works well with AWS, Azure, and Google Cloud.
    - Pre-installed Essentials: Comes with productivity apps, drivers, and media codecs.
    - Wayland Support: GNOME version offers native Wayland for improved performance.
    - Gaming & AI Ready: Supports Steam, Proton, and AI frameworks like TensorFlow.""",

    "Debian": """
    - Stability & Reliability: Debian Stable is known for its rock-solid performance, making it ideal for servers and workstations.  
    - Multiple Branches: Offers Stable, Testing, and Unstable versions, allowing users to choose between stability and cutting-edge software.  
    - Massive Software Repository: Over 59,000 packages available, covering everything from essential tools to specialized applications.  
    - Security Focused: Regular security updates and a dedicated team ensure a secure system.  
    - Cross-Platform Support: Runs on multiple architectures including x86, ARM, PowerPC, and RISC-V.  
    - Freedom & Open Source: Committed to free software principles, with non-free options available for those who need proprietary drivers.  
    - Customizable Installation: Offers netinstall, minimal, and full desktop installations with various desktop environments.  
    - Strong Community & Documentation: Backed by an extensive community and detailed documentation for troubleshooting and learning.""",

    "Linux Mint": """  
    - Windows-like Interface: Familiar UI for Windows users with Cinnamon, XFCE, and MATE versions.
    - Comes with Codecs: Multimedia support pre-installed for a smooth experience.
    - Cinnamon Desktop Environment: Modern, lightweight, and highly customizable.
    - Low System Requirements: Runs smoothly on older hardware.
    - Timeshift Backup: Simple system restore tool for easy recovery.
    - No Snap by Default: Uses traditional DEB packages, focusing on stability.
    - Software Manager: Easy-to-use app store with Flatpak support.
    - Optimized for Productivity: Works great for office and personal use.""",

    "Pop!_OS": """
    - Optimized for Productivity: Tiling window manager for better multitasking.
    - Built for Developers & Gamers: Pre-installed NVIDIA and AMD drivers.
    - Minimalist & Clean UI: GNOME-based, but with unique UI tweaks.
    - Auto-Stacking Windows: Improves workflow efficiency.
    - Flatpak Pre-installed: Allows access to latest software versions.
    - Encryption by Default: Security-focused with full-disk encryption.
    - System76 Support: Developed by a hardware manufacturer with performance tuning.
    - Rolling Release Model (Upcoming): Future updates will make it semi-rolling.""",

    "Zorin OS": """
    - Beginner-Friendly: Designed for users switching from Windows/macOS.
    - Zorin Appearance: Change layouts to match Windows or macOS.
    - Fast Performance: Optimized for speed on old and new hardware.
    - Pre-installed Software: Includes essentials for daily tasks like office tools.
    - Gaming-Ready: Built-in support for Steam, Lutris, and Wine.
    - Privacy-Focused: No data tracking or ads.
    - Lite Version Available: Uses XFCE for lightweight performance on older PCs.
    - Zorin Connect: Android phone integration for notifications and file sharing.""",

    "Fedora Workstation": """
    - Cutting-edge Software: Latest GNOME, Kernel, and tools before other distros.
    - Strong Security Features: SELinux and robust sandboxing for applications.
    - Flatpak & Wayland Support: Modern packaging and display server.
    - Red Hat Backing: Enterprise-level reliability and future-ready innovations.
    - Workstation & Server Editions: Available for different use cases.
    - No Proprietary Code by Default: Focuses on open-source, but can install proprietary drivers.
    - dnf Package Manager: Efficient, secure, and supports modular packages.
    - Immutable Fedora Silverblue Variant: Ideal for container-based development.""",

    "Nobara": """
    - Optimized for Gaming: Pre-installed with Proton, Wine, and gaming drivers.
    - Fedora-Based Stability: Uses Fedora’s core but adds gaming tweaks.
    - Media Codecs Pre-installed: Plays all formats without extra setup.
    - Custom Kernel Tweaks: Improves game performance and reduces latency.
    - Optimized for AMD & NVIDIA: Works out-of-the-box for gaming hardware.
    - Flatpak & AppImage Support: Ready for modern software distribution.
    - Streamlined Installer: Simple setup with user-friendly defaults.
    - Works for Creative Professionals: Supports Blender, DaVinci Resolve, and multimedia tools.""",

    "NixOS": """
    - Declarative System Configuration: System setup is defined in a single configuration file, making it reproducible and easy to manage.  
    - Atomic Upgrades & Rollbacks: System updates are transactional, allowing users to roll back to previous states if needed.  
    - Immutable Root Filesystem: The base system remains unchanged unless explicitly configured, enhancing security and consistency.  
    - Reproducible Builds: Ensures that installations are identical across different machines, making it ideal for DevOps and server environments.  
    - Nix Package Manager: A powerful package management system that avoids dependency conflicts through isolated environments.  
    - Multi-User Package Management: Allows different users to have separate package environments without affecting the system globally.  
    - Minimal Base System: Comes with only essential software, letting users customize the system as they see fit.  
    - Strong Community & Documentation: Supported by an active community and extensive documentation for both new and advanced users.""",

    "openSUSE": """
    - Two Versions: Leap (stable, enterprise-grade) and Tumbleweed (rolling release).
    - YaST Control Center: Centralized system administration tool.
    - Enterprise-Level Stability: Used in corporate environments.
    - Strong Security: Includes AppArmor, Btrfs snapshots, and secure boot options.
    - Zypper Package Manager: Reliable dependency handling with great performance.
    - Btrfs & XFS Support: Advanced file systems for reliability and performance.
    - Works for Developers: Great for coding, AI/ML, and embedded systems.
    - Rolling Release Option: Tumbleweed is cutting-edge, yet stable.""",

    "Manjaro": """
    - User-friendly Arch: Simplifies Arch installation with a graphical installer.
    - Hardware Detection: Auto-installs required drivers, including proprietary ones.
    - Stable Rolling Release: Updates go through testing before being released.
    - Multiple Desktop Environments: KDE, XFCE, GNOME editions available.
    - Pamac Package Manager: Easy GUI-based software installation.
    - AUR Access: Supports Arch User Repository with additional software.
    - Flatpak, Snap, and AppImage Support: Access to all major package formats.
    - Minimal & Full ISO Options: Choose a lightweight or feature-rich version.""",

    "EndeavourOS": """  
    - Close to Pure Arch: Simple, lightweight, and minimalistic.
    - Community-Driven: Excellent support forums and Arch Wiki resources.
    - Graphical Installer: No need for manual Arch setup (Calamares installer).
    - Rolling Release Model: Always up to date with the latest packages.
    - Xfce Default, but Customizable: Choose your preferred DE after installation.
    - AUR Support: Access to Arch’s massive software repository.
    - Minimal Bloatware: Only necessary software installed.
    - Great for Advanced Users: Encourages learning by doing.""",

    "Arch Linux": """
    - Minimalist & Customizable: Install only what you need, no unnecessary bloatware.
    - Rolling Release Model: Always up to date with the latest packages.
    - Pacman Package Manager: Fast and efficient package management.
    - AUR (Arch User Repository): Community-driven repository with thousands of extra packages.
    - Arch Wiki: One of the best documentation resources in the Linux world.
    - Manual Installation: Gives full control over system setup and configuration.
    - Lightweight & Performance-Oriented: Uses fewer system resources, great for power users.
    - Wayland & PipeWire Support: Modern display and audio systems included.""",
}
