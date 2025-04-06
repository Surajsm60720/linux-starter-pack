from distro_package_managers import DISTRO_FAMILIES

def load_installation_commands(distro: str):
    """Load installation commands based on distro family"""
    
    # Get the distro family
    family = DISTRO_FAMILIES.get(distro, "debian")
    
    # Import the appropriate commands module
    if family == "debian":
        from distros.ubuntu import INSTALLATION_COMMANDS
    elif family == "fedora":
        from distros.fedora import INSTALLATION_COMMANDS
    elif family == "arch":
        from distros.arch import INSTALLATION_COMMANDS
    elif family == "opensuse":
        from distros.opensuse import INSTALLATION_COMMANDS
    elif family == "nix":
        from distros.nixos import INSTALLATION_COMMANDS
    else:
        raise ValueError(f"Unsupported distribution family: {family}")
    
    return INSTALLATION_COMMANDS