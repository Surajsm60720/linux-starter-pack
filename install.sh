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
python3 -m pip install --user textual pyfiglet

echo "Installation complete!"