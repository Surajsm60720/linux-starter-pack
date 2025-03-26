from textual.app import App, ComposeResult
from textual.widgets import Header, Input, Footer, Markdown, Button, Label, Static
from textual.containers import Container, Horizontal, VerticalScroll
from textual.screen import Screen

class DistroOption(Markdown):
    
    def __init__(self, name: str) -> None:
        super().__init__(f"{name}\n")
        self._name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value


class DistroSelectScreen(Screen):

    CSS = """
    #DistroOption {
        background: $primary 10%;
        color: $text;
        margin: 1;
        padding: 1 2;
        text-style: bold;
    }

    #app-grid {
    layout: grid;
    grid-size: 2;  /* two columns */
    grid-columns: 1fr;
    grid-rows: 1fr;
    }

    #left-pane {
        align: center middle;
        width: 100%;
        height: 100%;
        row-span: 1;
        border: dodgerblue;
        opacity: 100%;
    }

    #top-right {       
        background: $panel;
        height: 100%;
        background: $panel;
        border: mediumvioletred;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("One", classes="box")
        yield Static("Two", classes="box")

    BINDINGS = [("escape", "go_back", "Back to Welcome"),
                ("q", "quit", "Quit"),
                ("up", "select_previous", "Select Previous Distro"),
                ("down", "select_next", "Select Next Distro"),]
    
    def action_quit(self) -> None:
        self.app.exit()

    def action_go_back(self) -> None:
        self.app.pop_screen()   
      
    def action_select_previous(self) -> None:
        """Select the previous distro option."""
        if self.selected_index > 0:
            self.selected_index -= 1
            self.update_selection()

    def action_select_next(self) -> None:
        """Select the next distro option."""
        if self.selected_index < len(self.distro_options) - 1:
            self.selected_index += 1
            self.update_selection()

    def compose(self) -> ComposeResult:
        with Container(id="app-grid"):
            with VerticalScroll(id="left-pane"):
                yield DistroOption("Ubuntu")
                yield DistroOption("Debian")
                yield DistroOption("Fedora")
                yield DistroOption("Arch")
            with Horizontal(id="top-right"):
                yield Static("Horizontally")
        
        yield Footer()