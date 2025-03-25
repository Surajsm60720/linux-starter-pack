from textual.app import App, ComposeResult
from textual.widgets import Header, Input, Footer, Markdown, Button, Label, Static
from textual.containers import VerticalScroll, Center
from textual.screen import Screen

class WelcomeScreen(Screen):
    """Welcome screen that prompts users to get started."""
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the welcome screen."""
        yield Header(show_clock=True)
        
        with Center():
            yield Label("Welcome to LinuxHelper TUI", id="title")
            yield Label("Your interactive terminal assistant", id="subtitle")
            yield Button("Get Started", variant="primary", id="start-button")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press event."""
        if event.button.id == "start-button":
            self.app.push_screen("distro_select")


class DistroOption(Markdown):
    """A selectable distro option."""
    
    def __init__(self, name: str, description: str) -> None:
        """Initialize with distro name and description."""
        super().__init__(f"{name}\n{description}")
        self._name = name
        self.description = description
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
    
    def on_click(self) -> None:
        """Handle click event."""
        self.app.selected_distro = self.name
        self.app.notify(f"You selected: {self.name}")


class DistroSelectScreen(Screen):
    """Screen for selecting a Linux distribution."""
    
    BINDINGS = [("escape", "go_back", "Back to Welcome")]
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the distro selection screen."""
        yield Header(show_clock=True)
        yield Label("Select Your Linux Distribution", id="selection-title")
        
        with VerticalScroll(id="distro-list"):
            yield DistroOption("Ubuntu", "Popular desktop distribution based on Debian")
            yield DistroOption("Fedora", "Community distribution sponsored by Red Hat")
            yield DistroOption("Arch Linux", "Lightweight and flexible Linux distribution")
            yield DistroOption("Debian", "Stable distribution that's the base for many others")
            yield DistroOption("Linux Mint", "User-friendly desktop distribution")
            yield DistroOption("openSUSE", "Stable and complete Linux distribution")
            yield DistroOption("CentOS", "Enterprise-class Linux Distribution derived from RHEL")
            yield DistroOption("Manjaro", "User-friendly Arch-based distribution")
            yield DistroOption("Elementary OS", "Fast and open replacement for Windows and macOS")
            yield DistroOption("Pop!_OS", "Ubuntu-based distro by System76")
        
        yield Footer()
    
    def action_go_back(self) -> None:
        """Go back to the welcome screen."""
        self.app.pop_screen()


class LinuxHelperApp(App):
    """Main application class."""
    
    AUTO_FOCUS = "Input"

    CSS = """
    #title {
        text-align: center;
        text-style: bold;
        color: $accent;
        margin: 1 0;
    }

    #subtitle {
        text-align: center;
        text-style: bold;
        color: $text;
        margin: 1 0;
    }

    DistroOption {
        background: $primary 10%;
        color: $text;
        margin: 1;
        padding: 1 2;
        text-style: bold;
    }
    """

    SCREENS = {
        "welcome": WelcomeScreen,
        "distro_select": DistroSelectScreen,
    }

    def compose(self) -> ComposeResult:
        """Compose the main application."""
        yield WelcomeScreen()
        yield DistroSelectScreen()

    def on_mount(self) -> None:
        """Set the initial state of the app."""
        self.selected_distro = None
        self.push_screen("welcome")  # Ensure you push the welcome screen


if __name__ == "__main__":
    app = LinuxHelperApp()  # Create an instance of the app
    app.run()               # Call the run method on the instance