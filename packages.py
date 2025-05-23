PACKAGE_DETAILS = {
    "Web Browsers": {
        "Chromium": 
            #"Command: sudo apt install chromium-browser\n"
            "Description:\n"
                "Chromium is an open-source web browser project that serves as the base for Google Chrome. "
                "It provides a fast and secure browsing experience while maintaining a high level of customizability. "
                "\n\n🔹 Common Use Cases:\n"
                "- Secure and private web browsing\n"
                "- Testing web applications on an open-source browser\n"
                "- Running lightweight browser-based applications\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `chromium-browser`\n"
                "- Check version: `chromium-browser --version`",
        "Google Chrome":
            #"Command: wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && sudo dpkg -i google-chrome-stable_current_amd64.deb\n"
            "Description:\n"
                "Google Chrome is a fast and widely used web browser known for its performance, security, and extensive extension support. "
                "It is popular among developers and casual users alike due to its seamless Google service integration. "
                "\n\n🔹 Common Use Cases:\n"
                "- Web browsing with extensive extension support\n"
                "- Syncing across multiple devices\n"
                "- Developer-friendly tools for web development\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `google-chrome`\n"
                "- Incognito mode: `google-chrome --incognito`",
        "Vivaldi":
            #"Command: wget -qO- https://downloads.vivaldi.com/stable/vivaldi-stable_amd64.deb | sudo dpkg -i\n"
            "Description:\n"
                "Vivaldi is a privacy-focused and highly customizable web browser with built-in features like a notes manager, screenshot tool, and tab stacking. "
                "It offers a unique browsing experience tailored to power users. "
                "\n\n🔹 Common Use Cases:\n"
                "- Privacy-focused web browsing\n"
                "- Multi-tab organization and productivity tools\n"
                "- Built-in customization and theming options\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `vivaldi`\n"
                "- Enable dark mode: `vivaldi --force-dark-mode`",
        "Opera": 
            #"Command: wget -qO- https://download3.operacdn.com/pub/opera/desktop/109.0.5097.41/linux/opera-stable_109.0.5097.41_amd64.deb | sudo dpkg -i -\n"
            "Description:\n"
                "Opera is a fast and feature-rich web browser with a built-in VPN, ad blocker, and sidebar integrations for chat apps like WhatsApp and Messenger. "
                "It offers a clean user interface, customizable workspaces, and speed optimizations for modern browsing. "
                "\n\n🔹 Common Use Cases:\n"
                "- Secure and private browsing with the built-in VPN\n"
                "- Accessing chat applications directly from the browser sidebar\n"
                "- Using built-in ad-blocking for faster page loads\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `opera`\n"
                "- Enable VPN: Go to `Settings > Privacy & Security > Enable VPN`\n"
                "- Speed Dial: Customize homepage shortcuts with `opera://startpage`",
        "Brave": 
            #"Command: curl -fsSL https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt update && sudo apt install brave-browser\n"
            "Description:\n" 
                "Brave is a privacy-focused web browser designed to block ads and trackers by default. "
                "It features a built-in Tor mode for anonymous browsing, Brave Rewards for earning cryptocurrency through privacy-friendly ads, and strong security measures.\n"
                "\n🔹 Common Use Cases:\n"
                "- Private browsing with built-in ad and tracker blocking\n"
                "- Anonymous browsing with Brave's built-in Tor window\n"
                "- Earning cryptocurrency (BAT) through Brave Rewards\n"
                "\n⚡ Extra Notes:"
                "- Launch: `brave-browser`\n"
                "- Open in private mode: `brave-browser --incognito`\n"
                "- Enable Tor mode: Open a new private window with Tor via `Menu > New Private Window with Tor`",
        "Zen Browser": 
            #"Command: (No official package; download manually from https://zen-browser.app)\n"
            "Description:\n"
                "Zen Browser is a lightweight, privacy-oriented browser focused on minimalism and distraction-free browsing. "
                "It is designed for users who prioritize simplicity, security, and low system resource usage. "
                "\n\n🔹 Common Use Cases:\n"
                "- Minimalist browsing with a clutter-free interface\n"
                "- Privacy-focused web surfing with minimal tracking\n"
                "- Low resource consumption for improved performance on older hardware\n"
                "\n⚡ Extra Notes:\n"
                "- Check settings for customization options like dark mode and script blocking",
    },

    "Development": {
        "git":
            #"Command: sudo apt install git\n"
            "Description:\n"
                "Git is a distributed version control system that tracks changes in source code, enabling collaboration and efficient project management. "
                "It is a must-have tool for developers working in teams. "
                "\n\n🔹 Common Use Cases:\n"
                "- Managing source code repositories\n"
                "- Collaborative software development with version control\n"
                "- Handling branching and merging in projects\n"
                "\n⚡ Extra Notes:\n"
                "- Check version: `git --version`\n"
                "- Configure: `git config --global user.name 'Your Name'`",
        "vim":
            #"Command: sudo apt install vim\n"
            "Description:\n"
                "Vim is a highly customizable text editor built for efficiency and speed. "
                "It is widely used for programming, scripting, and server administration. "
                "\n\n🔹 Common Use Cases:\n"
                "- Fast and efficient text editing\n"
                "- Remote server administration\n"
                "- Writing scripts and configuration files\n"
                "\n⚡ Extra Notes:\n"
                "- Open a file: `vim filename`\n"
                "- Exit: Press `Esc`, then type `:q!` to quit without saving or `:wq` to save and exit.",
        "Emacs": 
            #"Command: sudo apt install emacs\n"
            "Description:\n"
                "Emacs is a powerful, extensible, and customizable text editor that serves as an IDE, file manager, email client, and more. "
                "It supports thousands of extensions, making it highly versatile for programming, note-taking, and system administration. "
                "\n\n🔹 Common Use Cases:\n"
                "- Writing and editing code with built-in syntax highlighting\n"
                "- Using `org-mode` for efficient note-taking and project management\n"
                "- Running shell Commands and managing files without leaving Emacs\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `emacs`\n"
                "- Exit Emacs: Press `Ctrl + X` then `Ctrl + C`\n"
                "- Open tutorial: Run `emacs` and type `Ctrl + H` then `T`\n"
                "- Use Evil Mode for Vim keybindings: `M-x package-install RET evil RET`",      
        "Make": 
            #"Command: sudo apt install make\n"
            "Description:\n"
                "Make is a build automation tool used to compile and link programs efficiently. "
                "It processes `Makefile` instructions to determine which parts of a program need recompiling and executes only the necessary tasks. "
                "\n\n🔹 Common Use Cases:\n"
                "- Automating software compilation and project builds\n"
                "- Running predefined workflows in `Makefile`\n"
                "- Managing dependencies in large projects\n"
                "\n⚡ Extra Notes:\n"
                "- Check version: `make --version`\n"
                "- Run Makefile: `make`\n"
                "- Debug Makefile execution: `make --debug=v`",       
        "CMake": 
            #"Command: sudo apt install cmake\n"
            "Description:\n"
                "CMake is a cross-platform build system generator that simplifies project compilation across multiple environments. "
                "It automates the process of generating Makefiles or project files for compilers like GCC, Clang, and MSVC. "
                "\n\n🔹 Common Use Cases:\n"
                "- Generating Makefiles or Ninja build scripts\n"
                "- Managing multi-platform build configurations\n"
                "- Compiling C/C++ projects with ease\n"
                "\n⚡ Extra Notes:\n"
                "- Check version: `cmake --version`\n"
                "- Generate Makefile: `cmake .`\n"
                "- Build project: `cmake --build .`\n"
                "- Clean build files: `rm -rf CMakeCache.txt CMakeFiles`", 
        "Python3-pip": 
            #"Command: sudo apt install python3-pip\n"
            "Description:\n"
                "pip is the package manager for Python that simplifies the installation, upgrading, and removal of Python libraries. "
                "It allows developers to easily manage dependencies and install packages from the Python Package Index (PyPI). "
                "\n\n🔹 Common Use Cases:\n"
                "- Installing Python libraries for development (e.g., `pip install requests`)\n"
                "- Managing virtual environments and dependencies\n"
                "- Automating software installations for Python-based projects\n"
                "\n⚡ Extra Notes:\n"
                "- Check version: `pip3 --version`\n"
                "- Install a package: `pip3 install package_name`\n"
                "- List installed packages: `pip3 list`\n"
                "- Upgrade pip: `pip3 install --upgrade pip`",
    },

    "Networking": {
        "net-tools": 
            #"Command: sudo apt install net-tools\n"
            "Description:\n"
                "net-tools is a package that provides essential networking utilities, including `ifconfig`, `netstat`, and `route`. "
                "It helps diagnose network issues, monitor network traffic, and configure network interfaces. "
                "\n\n🔹 Common Use Cases:\n"
                "- Checking network configurations and active connections\n"
                "- Monitoring network traffic using `netstat`\n"
                "- Troubleshooting IP routing with `route`\n"
                "\n⚡ Extra Notes:\n"
                "- Check IP and interfaces: `ifconfig`\n"
                "- View open ports: `netstat -tulnp`\n"
                "- Display routing table: `route -n`",
        "traceroute": 
            #"Command: sudo apt install traceroute\n"
            "Description:\n"
                "traceroute is a diagnostic tool that maps the path packets take from a local system to a remote host. "
                "It identifies network latency and routing issues by displaying each hop along the route. "
                "\n\n🔹 Common Use Cases:\n"
                "- Diagnosing network slowdowns and packet loss\n"
                "- Identifying routing paths to remote servers\n"
                "- Detecting firewall or ISP-imposed restrictions\n"
                "\n⚡ Extra Notes:\n"
                "- Basic usage: `traceroute example.com`\n"
                "- Use TCP instead of UDP: `traceroute -T example.com`\n"
                "- Increase the number of probes: `traceroute -q 5 example.com`",
        "ping": 
            #"Command: sudo apt install iputils-ping\n"
            "Description:\n"
                "ping is a network utility that tests connectivity between two devices using ICMP echo requests. "
                "It measures response time and helps troubleshoot network reachability issues. "
                "\n\n🔹 Common Use Cases:\n"
                "- Checking if a website or server is reachable\n"
                "- Measuring network latency and packet loss\n"
                "- Diagnosing local and remote connectivity issues\n"
                "\n⚡ Extra Notes:\n"
                "- Basic test: `ping example.com`\n"
                "- Limit number of pings: `ping -c 5 example.com`\n"
                "- Adjust packet size: `ping -s 1000 example.com`",
    },

    "IDEs": {
        "VS Code":
            #"Command: sudo snap install code --classic\n"
            "Description:\n"
                "VS Code is a lightweight yet powerful code editor with built-in Git support, debugging tools, and an extensive extension marketplace. "
                "It is widely used for software development across multiple languages. "
                "\n\n🔹 Common Use Cases:\n"
                "- Developing applications in multiple programming languages\n"
                "- Debugging and running code efficiently\n"
                "- Using extensions for enhanced functionality\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `code`\n"
                "- Install extensions from the marketplace.",
        "PyCharm": 
            #"Command: sudo snap install pycharm-community --classic\n"
            "Description:\n"
                "PyCharm is a powerful Python IDE developed by JetBrains, featuring intelligent code assistance, debugging, and integration with frameworks like Django and Flask. "
                "It enhances productivity with code completion, error highlighting, and built-in tools for testing. "
                "\n\n🔹 Common Use Cases:\n"
                "- Developing Python applications efficiently\n"
                "- Debugging and profiling Python scripts\n"
                "- Managing virtual environments seamlessly\n"
                "\n⚡ Extra Notes:\n"
                "- Launch PyCharm: `pycharm`\n"
                "- Install plugins: Navigate to `Settings > Plugins`\n"
                "- Enable virtualenv: `Settings > Project > Python Interpreter`",
        "IntelliJ IDEA": 
            #"Command: sudo snap install intellij-idea-community --classic\n"
            "Description:\n"
                "IntelliJ IDEA is a Java-centric IDE by JetBrains, offering advanced code completion, debugging, and refactoring tools. "
                "It supports multiple languages, integrates with build tools like Maven and Gradle, and provides a smooth development experience. "
                "\n\n🔹 Common Use Cases:\n"
                "- Java development with smart code assistance\n"
                "- Working with frameworks like Spring and Hibernate\n"
                "- Managing complex projects with Git integration\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `intellij-idea-community`\n"
                "- Open an existing project: `File > Open`\n"
                "- Debug a Java application: `Run > Debug`",
        "Eclipse": 
            #"Command: sudo snap install eclipse --classic\n"
            "Description:\n"
                "Eclipse is an open-source IDE primarily used for Java development, but it also supports Python, C++, and web technologies through plugins. "
                "It includes powerful refactoring tools, a built-in debugger, and extensive customization options. "
                "\n\n🔹 Common Use Cases:\n"
                "- Java and Android development\n"
                "- Extending features with Eclipse Marketplace plugins\n"
                "- Managing large enterprise applications\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `eclipse`\n"
                "- Install new plugins: `Help > Eclipse Marketplace`\n"
                "- Configure workspaces: `File > Switch Workspace`",
        "Android Studio": 
            #"Command: sudo snap install android-studio --classic\n"
            "Description:\n"
                "Android Studio is the official IDE for Android development, providing a rich UI editor, code completion, and emulator support. "
                "It integrates with Gradle for project builds and supports Kotlin, Java, and Flutter development. "
                "\n\n🔹 Common Use Cases:\n"
                "- Building Android applications efficiently\n"
                "- Debugging mobile apps with built-in tools\n"
                "- Designing responsive UIs with Layout Editor\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `android-studio`\n"
                "- Create a new project: `File > New Project`\n"
                "- Run app on emulator: `Tools > AVD Manager`",
        "WebStorm": 
            #"Command: sudo snap install webstorm --classic\n"
            "Description:\n"
                "WebStorm is a JetBrains IDE for web development, offering intelligent code completion, debugging, and Git integration. "
                "It supports JavaScript, TypeScript, React, Angular, and Vue.js. "
                "\n\n🔹 Common Use Cases:\n"
                "- Frontend and backend JavaScript development\n"
                "- Debugging Node.js applications\n"
                "- Managing web frameworks efficiently\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `webstorm`\n"
                "- Install extensions: `Settings > Plugins`\n"
                "- Use live templates for faster coding",
        "Cursor": 
            #"Command: Not available in official repositories, download from official website\n"
            "Description:\n"
                "Cursor is an AI-powered code editor designed for efficient coding with real-time suggestions and AI-assisted debugging. "
                "It integrates with popular version control systems and enhances productivity for modern developers. "
                "\n\n🔹 Common Use Cases:\n"
                "- AI-powered code assistance for programming\n"
                "- Writing and refactoring large codebases quickly\n"
                "- Seamless integration with Git and cloud services\n"
                "\n⚡ Extra Notes:\n"
                "- Download from official site: `https://cursor.sh/`\n"
                "- Set up API keys for AI features\n"
                "- Customize themes and keybindings in settings",
    },

    "Multimedia": {
        "Spotify": 
            #"Command: sudo snap install spotify\n"
            "Description:\n"
                "Spotify is a digital music streaming service that provides access to millions of songs, podcasts, and playlists. "
                "It offers both free and premium subscriptions with offline listening and ad-free experiences. "
                "\n\n🔹 Common Use Cases:\n"
                "- Streaming music and podcasts\n"
                "- Creating and sharing playlists\n"
                "- Downloading songs for offline listening (Premium)\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `spotify`\n"
                "- Sign in with your Spotify account to sync playlists\n"
                "- Adjust audio quality in `Settings > Music Quality`",
        "Discord": 
            #"Command: sudo snap install discord\n"
            "Description:\n"
                "Discord is a popular VoIP, instant messaging, and digital distribution platform for communities and gamers. "
                "It supports voice channels, text chats, and screen sharing. "
                "\n\n🔹 Common Use Cases:\n"
                "- Gaming communication with friends and communities\n"
                "- Voice and video calls with screen sharing\n"
                "- Organizing communities via Discord servers\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `discord`\n"
                "- Use `/` Commands for quick actions\n"
                "- Customize notifications in `User Settings > Notifications`",
        "VLC":
            #"Command: sudo apt install vlc\n"
            "Description:\n"
                "VLC is an open-source, cross-platform media player that supports a wide variety of audio and video formats. "
                "It is known for its ability to play almost any media file. "
                "\n\n🔹 Common Use Cases:\n"
                "- Playing audio and video files\n"
                "- Streaming media from online sources\n"
                "- Converting media file formats\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `vlc`\n"
                "- Convert files: `vlc -I dummy input.mp4 --sout='#transcode{vcodec=h264}:std{access=file,dst=output.mp4}' vlc://quit`",
        "mpv": 
            #"Command: sudo apt install mpv\n"
            "Description:\n"
                "mpv is a lightweight, open-source media player based on MPlayer and mplayer2. "
                "It supports a wide range of video and audio formats with GPU acceleration. "
                "\n\n🔹 Common Use Cases:\n"
                "- Playing high-quality video files with minimal CPU usage\n"
                "- Watching YouTube videos directly from the terminal\n"
                "- Using scripts and keybindings for advanced playback controls\n"
                "\n⚡ Extra Notes:\n"
                "- Basic usage: `mpv video.mp4`\n"
                "- Stream online videos: `mpv <URL>`\n"
                "- Enable subtitles automatically: `mpv --sub-auto=fuzzy video.mp4`",
        "Audacity": 
            #"Command: sudo apt install audacity\n"
            "Description:\n"
                "Audacity is a free, open-source audio editing software used for recording, editing, and processing audio. "
                "It supports multi-track editing, effects, and plugins. "
                "\n\n🔹 Common Use Cases:\n"
                "- Recording and editing podcasts or voiceovers\n"
                "- Enhancing audio quality with noise reduction and equalization\n"
                "- Exporting audio in multiple formats (MP3, WAV, FLAC)\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `audacity`\n"
                "- Import audio: `File > Import`\n"
                "- Apply effects: `Effects > Equalization, Noise Reduction`",
        "ffmpeg": 
            #"Command: sudo apt install ffmpeg\n"
            "Description:\n"
                "ffmpeg is a powerful Command-line tool for processing video and audio files. "
                "It can convert, record, and stream multimedia files with support for multiple codecs. "
                "\n\n🔹 Common Use Cases:\n"
                "- Converting video formats (MP4, MKV, AVI, etc.)\n"
                "- Extracting audio from videos\n"
                "- Streaming and screen recording\n"
                "\n⚡ Extra Notes:\n"
                "- Convert a video: `ffmpeg -i input.mp4 output.avi`\n"
                "- Extract audio: `ffmpeg -i video.mp4 -vn -acodec copy audio.mp3`\n"
                "- Resize video: `ffmpeg -i input.mp4 -vf scale=1280:720 output.mp4`",
    },

    "Terminals": {
        "Kitty":
            #"Command: sudo apt install kitty\n"
            "Description:\n"
                "Kitty is a fast, feature-rich terminal emulator with GPU acceleration and advanced text rendering. "
                "It is highly customizable and supports tabs, splits, and scripting. "
                "\n\n🔹 Common Use Cases:\n"
                "- Running shell Commands efficiently\n"
                "- Handling multiple terminal tabs/splits\n"
                "- Using hardware acceleration for faster rendering\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `kitty`\n"
                "- Customize config: `~/.config/kitty/kitty.conf`",
       "Alacritty": 
            #"Command: sudo apt install alacritty\n"
            "Description:\n"
                "Alacritty is a GPU-accelerated terminal emulator known for its speed and simplicity. "
                "It supports OpenGL rendering for fast performance. "
                "\n\n🔹 Common Use Cases:\n"
                "- Using a lightweight and fast terminal for development\n"
                "- Customizing themes and keybindings via `alacritty.yml`\n"
                "- Running multiple shell sessions efficiently\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `alacritty`\n"
                "- Customize: Edit `~/.config/alacritty/alacritty.yml`\n"
                "- Increase font size: `Ctrl + Shift + Plus`",
        "Wezterm": 
            #"Command: Download from https://wezfurlong.org/wezterm/\n"
            "Description:\n"
                "WezTerm is a modern, GPU-accelerated terminal emulator with support for tabs, multiplexing, and SSH integration. "
                "It is highly configurable and supports features like ligatures and remote connections. "
                "\n\n🔹 Common Use Cases:\n"
                "- Running a powerful and customizable terminal\n"
                "- Using SSH and remote server management\n"
                "- Creating workspaces with multiple terminal panes\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `wezterm`\n"
                "- Configure settings in `~/.wezterm.lua`\n"
                "- Split terminal: `Ctrl + Shift + D`",
    },

    "Graphics": {
        "Okular": 
            #"Command: sudo apt install okular\n"
            "Description:\n"
                "Okular is a versatile document viewer developed by KDE. "
                "It supports multiple file formats, including PDF, EPUB, DjVu, and more. "
                "With its annotation and text extraction features, Okular is ideal for both casual reading and professional document management. "
                "\n\n🔹 Common Use Cases:\n"
                "- Reading PDFs and EPUB books\n"
                "- Annotating documents with highlights and notes\n"
                "- Extracting text from PDFs and scanned documents\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `okular`\n"
                "- Use `F6` to activate annotation tools\n"
                "- Search within documents using `Ctrl + F`",
        "Scribus": 
            #"Command: sudo apt install scribus\n"
            "Description:\n"
                "Scribus is an open-source desktop publishing (DTP) application used for creating professional-quality layouts. "
                "It is ideal for designing magazines, brochures, flyers, and books, offering advanced typography and PDF export features. "
                "\n\n🔹 Common Use Cases:\n"
                "- Designing print-ready publications and layouts\n"
                "- Creating professional PDF documents with high-quality typography\n"
                "- Producing newsletters, posters, and business cards\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `scribus`\n"
                "- Enable color management for print design under `Preferences > Color Management`",
        "Gimp":
            #"Command: sudo apt install gimp\n"
            "Description:\n"
                "GIMP (GNU Image Manipulation Program) is a powerful open-source image editor, comparable to Photoshop. "
                "It is used for photo retouching, image composition, and graphic design. "
                "\n\n🔹 Common Use Cases:\n"
                "- Editing and retouching images\n"
                "- Creating digital artwork and graphics\n"
                "- Designing UI elements\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `gimp`\n"
                "- Supports plugins and scripting with Python.",
        "Inkscape": 
            #"Command: sudo apt install inkscape\n"
            "Description:\n"
                "Inkscape is a professional vector graphics editor for creating illustrations, icons, logos, and more. "
                "It supports SVG and various export formats. "
                "\n\n🔹 Common Use Cases:\n"
                "- Designing vector illustrations and UI elements\n"
                "- Editing and converting SVG files\n"
                "- Creating logos and digital art\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `inkscape`\n"
                "- Save projects in `.svg` format for scalability\n"
                "- Use `Extensions > Color > Remove Background` to edit images",
        "Blender": 
            #"Command: sudo apt install blender\n"
            "Description:\n"
                "Blender is an open-source 3D modeling and animation software. "
                "It supports rendering, sculpting, simulation, and video editing. "
                "\n\n🔹 Common Use Cases:\n"
                "- Creating 3D models and animations\n"
                "- Simulating physics-based effects\n"
                "- Rendering high-quality graphics\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `blender`\n"
                "- Use `E` for extrude and `Ctrl + R` for edge loops\n"
                "- Enable GPU rendering for faster processing",
        "ImageMagick": 
            #"Command: sudo apt install imagemagick\n"
            "Description:\n"
                "ImageMagick is a powerful Command-line tool for editing, converting, and processing images. "
                "It supports a wide range of image formats and can perform batch operations efficiently. "
                "\n\n🔹 Common Use Cases:\n"
                "- Converting images between different formats (PNG, JPEG, TIFF, etc.)\n"
                "- Resizing and compressing images for web optimization\n"
                "- Applying filters and effects via Command-line scripts\n"
                "\n⚡ Extra Notes:\n"
                "- Convert images: `convert input.png output.jpg`\n"
                "- Resize images: `convert input.jpg -resize 800x600 output.jpg`\n"
                "- Batch convert PNG to JPG: `mogrify -format jpg *.png`",
    },

    "System Tools": {
        "Gparted":
            #"Command: sudo apt install gparted\n"
            "Description:\n"
                "GParted is a powerful partition manager that allows users to create, resize, and manage disk partitions. "
                "It is widely used for disk maintenance and system recovery. "
                "\n\n🔹 Common Use Cases:\n"
                "- Resizing and formatting disk partitions\n"
                "- Managing disk space efficiently\n"
                "- Troubleshooting and repairing storage devices\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `gparted`\n"
                "- Requires root privileges to modify partitions.",
        "Disks": 
            #"Command: sudo apt install gnome-disk-utility\n"
            "Description:\n"
                "GNOME Disks is a graphical tool for managing hard drives and partitions. "
                "It allows users to format, mount, and benchmark disks easily. "
                "\n\n🔹 Common Use Cases:\n"
                "- Checking disk health and SMART status\n"
                "- Formatting and partitioning drives\n"
                "- Creating and restoring disk images\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `gnome-disks`\n"
                "- Create a bootable USB: `Restore Disk Image > Select ISO`\n"
                "- Run performance benchmark: `Disks > Benchmark`",
        "BleachBit": 
            #"Command: sudo apt install bleachbit\n"
            "Description:\n"
                "BleachBit is a disk cleaning utility that frees up space and protects privacy by removing unnecessary files. "
                "It cleans system caches, logs, and temporary files. "
                "\n\n🔹 Common Use Cases:\n"
                "- Deleting junk files to free up space\n"
                "- Securely wiping sensitive data\n"
                "- Cleaning browser history and cookies\n"
                "\n⚡ Extra Notes:\n"
                "- Launch: `bleachbit`\n"
                "- Clean system files: `sudo bleachbit --clean system.*`\n"
                "- Shred files securely: `bleachbit --shred <file>`",
    },
}
