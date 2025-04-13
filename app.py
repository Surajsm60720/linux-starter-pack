from textual.app import App, ComposeResult
from textual.widgets import Footer, Label
from textual.containers import Center
from textual.screen import Screen
from distro import DistroSelectScreen
import pyfiglet
from confirm_screen import ConfirmationScreen
from shared_types import SharedCart
from essential_packages import commands  # Import the essential packages dictionary

ascii_text = pyfiglet.figlet_format("Linux Starter Pack", font = "doom")

class WelcomeScreen(Screen):

    BINDINGS = [
        ("enter", "distro_select", "Next Screen"),
        ("q", "quit", "Quit")
    ]
    
    def action_quit(self) -> None:
        self.app.exit()

    def action_distro_select(self) -> None:
        self.app.push_screen("distro_select")
    
    def compose(self) -> ComposeResult:
        
        with Center():
            yield Label(ascii_text,id="title")
            yield Label("A quick way to install packages in your Linux system", id="subtitle")
        
        yield Footer()

class App(App):
    
    AUTO_FOCUS = "Input"

    CSS = """
    #title {
        align: center middle;
        text-align: center;
        color: lightseagreen;
        width: 100%;
        margin: 1 0;
    }

    #subtitle {
        text-align: center;
        text-style: bold;
        color: $text;
        margin: 1 0;
        width: 100%;
    }
    """

    SCREENS = {
        "welcome": WelcomeScreen,
        "distro_select": DistroSelectScreen,
    }

    def compose(self) -> ComposeResult:
        yield WelcomeScreen()
        yield DistroSelectScreen()

    def on_mount(self) -> None:
        self.selected_distro = None
        SharedCart.clear()  # Initialize shared cart
        self.selected_packages = []
        self.script_path = "install_packages.sh"
        self.push_screen("welcome")

        # Initialize bash script with package manager setup
        with open(self.script_path, "w") as script_file:
            script_file.write("#!/bin/bash\n\n")
            script_file.write("echo 'Starting package installation...'\n\n")
            script_file.write("# Update package lists and install essential tools\n")
            script_file.write(self.get_essential_commands())

    def get_essential_commands(self) -> str:
        """Get essential commands based on the selected distro"""
        if self.selected_distro in commands:
            return commands[self.selected_distro]
        return "echo 'No essential commands defined for this distribution.'\n"

    def update_selected_distro(self, distro: str) -> None:
        """Update the selected distro and reinitialize the script"""
        self.selected_distro = distro
        # Reinitialize script with new distro-specific commands
        with open(self.script_path, "w") as script_file:
            script_file.write("#!/bin/bash\n\n")
            script_file.write("echo 'Starting package installation...'\n\n")
            script_file.write("# Essential commands for the selected distro\n")
            script_file.write(self.get_essential_commands())

    def show_confirmation_screen(self) -> None:
        self.selected_packages = SharedCart.get_items()  # Use SharedCart method
        self.push_screen(ConfirmationScreen(self.selected_packages, self.script_path))

if __name__ == "__main__":
    App().run()