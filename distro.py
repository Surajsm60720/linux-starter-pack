from textual.app import App, ComposeResult
from textual.widgets import Header, Input, Footer, Markdown, Button, Label, Static
from textual.containers import VerticalScroll, Center
from textual.screen import Screen

class DistroOption(Markdown):
    
    def __init__(self, name: str, description: str) -> None:
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
        self.app.selected_distro = self.name
        self.app.notify(f"You selected: {self.name}")


class DistroSelectScreen(Screen):

    CSS = """
    #DistroOption {
        background: $primary 10%;
        color: $text;
        margin: 1;
        padding: 1 2;
        text-style: bold;
    }
    """
    
    BINDINGS = [("escape", "go_back", "Back to Welcome")]
    
    def compose(self) -> ComposeResult:
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
        self.app.pop_screen()
