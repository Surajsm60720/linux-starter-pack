# from textual.containers import Container, VerticalScroll, Horizontal
# from textual.screen import Screen
# from textual.reactive import reactive
# from textual.widgets import Static, Button, Markdown
# from textual.app import ComposeResult
# from categories import CATEGORIES_LIST
# from textual.widgets import Footer
# from package_select import PackageSelectorScreen

# class CategoryOption(Markdown):
#     def __init__(self, name: str) -> None:
#         super().__init__(f"**{name}**\n")
#         self._name = name

#     def get_name(self) -> str:
#         return self._name

# class CategorySelectScreen(Screen):

#     CSS = """
#     #distro-option {
#         background: $primary 10%;
#         color: $text;
#         margin: 1;
#         padding: 1 2;
#         text-style: bold;
#     }

#     #app-grid {
#         layout: grid;
#         grid-size: 2;
#         grid-columns: 1fr 2fr;
#         grid-rows: 1fr;
#         height: 100%;
#     }

#     #left-pane {
#         align: center middle;
#         width: 100%;
#         height: 100%;
#         border: dodgerblue;
#     }

#     #top-right {       
#         background: $panel;
#         height: 100%;
#         border: mediumvioletred;
#         padding: 1;
#     }

#     .selected {
#         background: $primary 50%;
#     }
#     """

#     selected_index = reactive(0)

#     def compose(self) -> ComposeResult:
#         with Container(id="app-grid"):
#             with VerticalScroll(id="left-pane"):
#                 self.category_options = [
#                     CategoryOption(name) for name in CATEGORIES_LIST
#                 ]
#                 for option in self.category_options:
#                     yield option
#             with Horizontal(id="top-right"):
#                 self.content_panel = Static(self.get_selected_content(), id="facts")
#                 yield self.content_panel

#         yield Footer()

#     BINDINGS = [
#         ("escape", "go_back", "Back to Welcome"),
#         ("q", "quit", "Quit"),
#         ("up", "select_previous", "Select Previous Distro"),
#         ("down", "select_next", "Select Next Distro"),
#         ("enter", "select_distro", "Select Distro"),
#     ]

#     def on_mount(self) -> None:
#         """Called when the screen is mounted."""
#         self.update_selection()

#     def get_selected_content(self) -> str:
#         selected_category = list(CATEGORIES_LIST.keys())[self.selected_index]
#         return CATEGORIES_LIST[selected_category]

#     def update_selection(self) -> None:
#         for i, option in enumerate(self.category_options):
#             option.remove_class("selected")
#         self.category_options[self.selected_index].add_class("selected")
#         self.content_panel.update(self.get_selected_content())

#     def action_select_previous(self) -> None:
#         if self.selected_index > 0:
#             self.selected_index -= 1
#             self.update_selection()

#     def action_select_next(self) -> None:
#         if self.selected_index < len(self.distro_options) - 1:
#             self.selected_index += 1
#             self.update_selection()

#     def action_select_distro(self) -> None:
#         selected_distro = list(CATEGORIES_LIST.keys())[self.selected_index]
#         package_screen = PackageSelectorScreen()
#         package_screen.selected_distro = selected_distro
#         self.app.push_screen(package_screen)

#     def action_quit(self) -> None:
#         self.app.exit()

#     def action_go_back(self) -> None:
#         self.app.pop_screen()

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Markdown, Static
from textual.containers import Container, VerticalScroll
from textual.reactive import reactive
from categories import CATEGORIES_LIST  # Importing categories
from package_select import PackageSelectorScreen  # Importing package selection screen

class CategoryOption(Markdown):
    """Represents a selectable category."""
    
    def __init__(self, name: str) -> None:
        super().__init__(f"**{name}**\n")
        self._name = name

    def get_name(self) -> str:
        return self._name


class CategorySelectScreen(Screen):
    """Displays categories available for installation on a selected distro."""

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
    }

    #right-pane {       
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
    selected_distro = ""

    def compose(self) -> ComposeResult:
        """Creates UI components for category selection."""
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

        yield Footer()

    BINDINGS = [
        ("escape", "go_back", "Back to Distro Select"),
        ("q", "quit", "Quit"),
        ("up", "select_previous", "Select Previous Category"),
        ("down", "select_next", "Select Next Category"),
        ("enter", "select_category", "Select Category"),
    ]

    def get_selected_category_info(self) -> str:
        """Retrieves category details dynamically."""
        category_name = list(CATEGORIES_LIST.keys())[self.selected_index]
        packages = "\n".join(f"- {pkg}" for pkg in CATEGORIES_LIST[category_name])
        return f"**{category_name}**\n\nAvailable Packages:\n{packages}"

    def update_selection(self) -> None:
        """Updates the selected category visually and refreshes details."""
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
        """Handle selection of a category (e.g., transition to package installation screen)."""
        selected_category = list(CATEGORIES_LIST.keys())[self.selected_index]
        self.app.push_screen(PackageSelectorScreen(selected_category, self.selected_distro))

    def action_quit(self) -> None:
        self.app.exit()

    def action_go_back(self) -> None:
        self.app.pop_screen()
