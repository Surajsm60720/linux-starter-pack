#!/bin/bash

echo "Installing Linux Starter Pack..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Installing Python 3..."
    if command -v apt &> /dev/null; then
        sudo apt update && sudo apt install -y python3 python3-pip
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y python3 python3-pip
    elif command -v pacman &> /dev/null; then
        sudo pacman -Sy --noconfirm python python-pip
    elif command -v zypper &> /dev/null; then
        sudo zypper install -y python3 python3-pip
    else
        echo "Could not install Python 3. Please install it manually."
        exit 1
    fi
fi

# Create temporary directory
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

# Download the package from GitHub
echo "Downloading Linux Starter Pack..."
curl -L -o main.zip https://github.com/Surajsm60720/linux-starter-pack/archive/main.zip

# Install unzip if not present
if ! command -v unzip &> /dev/null; then
    echo "Installing unzip..."
    if command -v apt &> /dev/null; then
        sudo apt install -y unzip
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y unzip
    elif command -v pacman &> /dev/null; then
        sudo pacman -Sy --noconfirm unzip
    elif command -v zypper &> /dev/null; then
        sudo zypper install -y unzip
    fi
fi

# Extract the package
unzip main.zip
cd linux-starter-pack-main

# Install requirements
echo "Installing dependencies..."
python3 -m pip install -r requirements.txt

# Make the app executable
chmod +x app.py

# Create desktop entry
echo "Creating desktop entry..."
cat > ~/.local/share/applications/linux-starter-pack.desktop << EOL
[Desktop Entry]
Name=Linux Starter Pack
Comment=A quick way to install packages in your Linux system
Exec=python3 $(pwd)/app.py
Icon=$(pwd)/icon.png
Terminal=false
Type=Application
Categories=Utility;
EOL

# Create a symbolic link to make it accessible from terminal
echo "Creating command line access..."
sudo ln -sf "$(pwd)/app.py" /usr/local/bin/linux-starter-pack

echo "Installation complete!"
echo "You can now run Linux Starter Pack by:"
echo "1. Searching for 'Linux Starter Pack' in your applications menu"
echo "2. Running 'linux-starter-pack' in terminal"