from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Markdown, Static
from textual.containers import Container, VerticalScroll
from textual.reactive import reactive
from categories import CATEGORIES_LIST 
from package_select import PackageSelectorScreen 

class CategoryOption(Markdown):
    
    def __init__(self, name: str) -> None:
        super().__init__(f"**{name}**\n")
        self._name = name

    def get_name(self) -> str:
        return self._name


class CategorySelectScreen(Screen):

    CSS = """
    #category-option {
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
        row-span: 2;
    }

    #right-pane {       
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
    selected_distro = ""

    def compose(self) -> ComposeResult:
        with Container(id="app-grid"):
            with VerticalScroll(id="left-pane"):
                self.category_options = [
                    CategoryOption(name) for name in CATEGORIES_LIST.keys()
                ]
                for option in self.category_options:
                    yield option
            with Container(id="right-pane"):
                self.details_panel = Static(self.get_selected_category_info(), id="details")
                yield self.details_panel
            with Container(id="bottom-right"):
                yield Static("Here comes the cart items")

        yield Footer()

    BINDINGS = [
        ("escape", "go_back", "Back to Distro Select"),
        ("q", "quit", "Quit"),
        ("up", "select_previous", "Select Previous Category"),
        ("down", "select_next", "Select Next Category"),
        ("enter", "select_category", "Select Category"),
    ]

    def get_selected_category_info(self) -> str:
        category_name = list(CATEGORIES_LIST.keys())[self.selected_index]
        packages = "\n".join(f"- {pkg}" for pkg in CATEGORIES_LIST[category_name])
        return f"{category_name}\n\nAvailable Packages:\n{packages}"

    def update_selection(self) -> None:
        for i, option in enumerate(self.category_options):
            option.remove_class("selected")
        self.category_options[self.selected_index].add_class("selected")

        self.details_panel.update(self.get_selected_category_info())

    def action_select_previous(self) -> None:
        if self.selected_index > 0:
            self.selected_index -= 1
            self.update_selection()

    def action_select_next(self) -> None:
        if self.selected_index < len(self.category_options) - 1:
            self.selected_index += 1
            self.update_selection()

    def action_select_category(self) -> None:
        selected_category = list(CATEGORIES_LIST.keys())[self.selected_index]
        self.app.push_screen(PackageSelectorScreen(selected_category))

    def action_quit(self) -> None:
        self.app.exit()

    def action_go_back(self) -> None:
        self.app.pop_screen()
