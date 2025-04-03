import importlib

def load_installation_commands(distro: str):
    # Map distro names to file names
    distro_files = {
        "Ubuntu": "ubuntu",
        "Debian": "ubuntu",  # Debian can reuse Ubuntu commands
        "Linux Mint": "ubuntu",
        "Pop!_OS": "ubuntu",
        "Zorin OS": "ubuntu",
        "Fedora Workstation": "fedora",
        "Nobara": "fedora",
        "openSUSE": "opensuse",
        "Manjaro": "arch_linux",
        "EndeavourOS": "arch_linux",
        "Arch Linux": "arch_linux",
        "NixOS": "nixos",
    }

    file_name = distro_files.get(distro)
    if not file_name:
        raise ValueError(f"No installation commands available for distro: {distro}")

    # Dynamically import the module
    module_path = f"package_installation_steps.{file_name}"
    module = importlib.import_module(module_path)
    return module.INSTALLATION_COMMANDS