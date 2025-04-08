## Linux Starter Pack

Linux, or sometimes as I like to call the OS where you are not just a user but a <b>developer</b> too, is having a huge list of variations 
in terms of even some basic features like the package managers to download the softwares between the plethora of distributions that its 
community has to offer.

## About the project

Linux Starter Pack is a command line tool that you can run in the terminal of your choice to install packages based on the Linux distribution you are on.<br>
The CLI tool has a TUI built completely in Python that helps in easier navigation and ability to make a bash script that can be found in the project directory.<br>
The bash script can be used by the user to add any other package or software installation commands which can be saved and used by them to automate installation of them all.

## Features

- **Cross-Distribution Support**: Works seamlessly on Ubuntu, Fedora, Arch, openSUSE, and more
- **Intuitive Interface**: Beautiful TUI (Terminal User Interface) for easy navigation
- **Smart Package Management**: Automatically uses the correct package manager for your distro
- **Pre-configured Tools**: Common development tools, browsers, and applications ready to install
- **Batch Installation**: Install multiple packages with a single command
- **Category-based Organization**: Easy browsing through categorized software
- **Safe and Transparent**: Review installation commands before execution
- **Fast and Efficient**: Optimized for quick installations

## Getting started

The easiest way to start using this tool is by running the following command: 

   ```bash
   curl -sSL https://raw.githubusercontent.com/Surajsm60720/linux-starter-pack/main/install.sh | bash 
   python3 app.py
   ```

If you want to manually install the package then follow the steps below,

1. Clone the repository:
   ```bash
    cd Downloads
    git clone https://github.com/Surajsm60720/linux-starter-pack.git
   ```
   Or simply download the file.

2. Run the following command in the terminal:
   ```bash
   cd /linux-starter-pack
   pip install -r textual pyfiglet
   python3 app.py
   ```

## Who Is This For?

### New Linux Users
- Easily install common software without memorizing commands
- Learn package management across different distributions
- Discover essential tools for development and daily use
### Power Users
- Quick setup for development environments
- Generate installation scripts for automation
- Consistent package installation across different distros

## Supported Software Categories
- Web Browsers: Chrome, Firefox, Brave, and more
- Development Tools: Git, VS Code, Python tools
- System Utilities: System monitors, disk tools
- Graphics Software: GIMP, Inkscape, Blender
- Multimedia: VLC, Spotify, audio tools
- Terminal Emulators: Kitty, Alacritty
- IDEs: PyCharm, IntelliJ IDEA, Eclipse
And many more.....

## Key Benefits
- Time-Saving: Install multiple packages in one go
- Learning Tool: Understand package management across distributions
- Error Prevention: Avoid common installation pitfalls
- Customizable: Choose what you need, skip what you don't
- Reproducible: Generate scripts for consistent setup across machines

## Acknowledgments
All the amazing Linux distribution maintainers, the open source community and the users of the project.<br>
A big shout out to the contributors of this project.
