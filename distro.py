from textual.app import ComposeResult
from textual.widgets import Footer, Markdown, Static
from textual.containers import Container, Horizontal, VerticalScroll
from textual.screen import Screen
from textual.reactive import reactive
from info import DISTRO_FACTS
from package_select import PackageSelectorScreen


class DistroOption(Markdown):
    def __init__(self, name: str) -> None:
        super().__init__(f"**{name}**\n")
        self._name = name

    def get_name(self) -> str:
        return self._name


class DistroSelectScreen(Screen):

    CSS = """
    #distro-option {
        background: $primary 10%;
        color: $text;
        margin: 1;
        padding: 1 2;
        text-style: bold;
    }

    #app-grid {
        layout: grid;
        grid-size: 2;
        grid-columns: 1fr 2fr;
        grid-rows: 1fr;
        height: 100%;
    }

    #left-pane {
        align: center middle;
        width: 100%;
        height: 100%;
        border: dodgerblue;
    }

    #top-right {       
        background: $panel;
        height: 100%;
        border: mediumvioletred;
        padding: 1;
    }

    .selected {
        background: $primary 50%;
    }
    """

    selected_index = reactive(0)

    def compose(self) -> ComposeResult:
        with Container(id="app-grid"):
            with VerticalScroll(id="left-pane"):
                self.distro_options = [
                    DistroOption(name) for name in DISTRO_FACTS.keys()
                ]
                for option in self.distro_options:
                    yield option
            with Horizontal(id="top-right"):
                self.facts_panel = Static(self.get_selected_fact(), id="facts")
                yield self.facts_panel

        yield Footer()

    BINDINGS = [
        ("escape", "go_back", "Back to Welcome"),
        ("q", "quit", "Quit"),
        ("up", "select_previous", "Select Previous Distro"),
        ("down", "select_next", "Select Next Distro"),
        ("enter", "select_distro", "Select Distro"),
    ]

    def get_selected_fact(self) -> str:
        return DISTRO_FACTS[list(DISTRO_FACTS.keys())[self.selected_index]]

    def update_selection(self) -> None:
        for i, option in enumerate(self.distro_options):
            option.remove_class("selected")
        self.distro_options[self.selected_index].add_class("selected")

        self.facts_panel.update(self.get_selected_fact())

    def action_select_previous(self) -> None:
        if self.selected_index > 0:
            self.selected_index -= 1
            self.update_selection()

    def action_select_next(self) -> None:
        if self.selected_index < len(self.distro_options) - 1:
            self.selected_index += 1
            self.update_selection()

    def action_select_distro(self) -> None:
        selected_distro = list(DISTRO_FACTS.keys())[self.selected_index]
        package_screen = PackageSelectorScreen()
        package_screen.selected_distro = selected_distro
        self.app.push_screen(package_screen)

    def action_quit(self) -> None:
        self.app.exit()

    def action_go_back(self) -> None:
        self.app.pop_screen()

