from textual.app import ComposeResult
from textual.widgets import Footer, Markdown, Static
from textual.containers import Container, Horizontal, VerticalScroll
from textual.screen import Screen
from textual.reactive import reactive
from packages import PACKAGE_DETAILS

class PackageSelectorScreen(Screen):

    def __init__(self, selected_category: str) -> None:
        self.selected_category = selected_category
        super().__init__()

    selected_distro = ""

    CSS = """
    #package-option {
        background: $primary 10%;
        color: $text;
        margin: 1;
        padding: 1 2;
        text-style: bold;
    }

    #app-grid {
        layout: grid;
        grid-size: 2;
        grid-columns: 1fr;
        grid-rows: 1fr;
    }

    #left-pane {
        width: 100%;
        height: 100%;
        border: dodgerblue;
        row-span: 2;
        background: $panel;
        border: dodgerblue;
    }

    #top-right {
        background: $panel;
        height: 100%;
        border: mediumvioletred;
        padding: 1;
    }

    #bottom-right {
        height: 100%;
        layout: grid;
        grid-size: 3;
        grid-columns: 2fr;
        grid-rows: 1fr;
        grid-gutter: 1;
        background: $panel;
        border: greenyellow;
    }

    .selected {
        background: $primary 50%;
    }
    """

    selected_index = reactive(0)

    def compose(self) -> ComposeResult:
        with Container(id="app-grid"):
            with VerticalScroll(id="left-pane"):
                self.package_options = [
                    Markdown(f"**{pkg}**")
                    for pkg, cmd in PACKAGE_DETAILS[self.selected_category].items()
                ]
                for option in self.package_options:
                    yield option
            with Horizontal(id="top-right"):
                self.command_panel = Static(self.get_selected_command(), id="commands")
                yield self.command_panel
            with Container(id="bottom-right"):
                yield Static("Here comes app cart items")

        yield Footer()
    
    BINDINGS=[
        ("escape", "go_back", "Back to Category Selection"),
        ("q", "quit", "Quit"),
        ("up", "select_previous", "Select Previous Package"),
        ("down", "select_next", "Select Next Package"),
    ]

    def get_selected_command(self) -> str:
        package_name = list(PACKAGE_DETAILS[self.selected_category].keys())[self.selected_index]
        return PACKAGE_DETAILS[self.selected_category][package_name]

    def update_selection(self) -> None:
        for i, option in enumerate(self.package_options):
            option.remove_class("selected")
        self.package_options[self.selected_index].add_class("selected")

        self.command_panel.update(self.get_selected_command())

    def action_select_previous(self) -> None:
        if self.selected_index > 0:
            self.selected_index -= 1
            self.update_selection()

    def action_select_next(self) -> None:
        
        if self.selected_index < len(self.package_options) - 1:
            self.selected_index += 1
            self.update_selection()
    
    def action_quit(self) -> None:
        self.app.exit()

    def action_go_back(self) -> None:
        self.app.pop_screen()
