from textual.app import ComposeResult
from textual.widgets import Footer, Markdown, Static
from textual.containers import Container, Horizontal, VerticalScroll, ScrollableContainer
from textual.screen import Screen
from textual.reactive import reactive
from packages import PACKAGE_DETAILS
from shared_types import SharedCart
from distros.ubuntu import INSTALLATION_COMMANDS

class PackageSelectorScreen(Screen):

    def __init__(self, selected_category: str) -> None:
        self.selected_category = selected_category
        super().__init__()

    selected_distro = ""
    cart = reactive([])

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
        padding: 1;
    }

    #cart-scroll {
        height: 100%;
        padding-right: 0;
        overflow-y: auto;
        padding: 0 1 0 1;
        margin: 0;
    }

    #package-cart-display {
        width: 100%;
        padding: 1;
        margin-right: 2;
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
                with ScrollableContainer(id="cart-scroll"):
                    self.cart_display = Static("Cart:\n", id="package-cart-display")
                    yield self.cart_display

        yield Footer()
    
    BINDINGS=[
        ("escape", "go_back", "Back to Categories"),
        ("q", "quit", "Quit"),
        ("up", "select_previous", "Select Previous Package"),
        ("down", "select_next", "Select Next Package"),
        ("enter", "add_to_cart", "Add Package to Cart"),
        ("r", "remove_from_cart", "Remove Package from Cart"),
        ("c", "confirm_selection", "Confirm Selection"),
    ]

    def action_go_back(self) -> None:
        # Update shared cart before going back
        self.app.pop_screen()

    def action_add_to_cart(self) -> None:
        package_name = list(PACKAGE_DETAILS[self.selected_category].keys())[self.selected_index]
        self.update_cart(package_name, add=True)

    def action_remove_from_cart(self) -> None:
        package_name = list(PACKAGE_DETAILS[self.selected_category].keys())[self.selected_index]
        self.update_cart(package_name, add=False)

    def update_cart(self, package_name: str, add: bool) -> None:
        if add:
            if package_name not in SharedCart.items:  # Use SharedCart instead of self.cart
                SharedCart.add_item(package_name)  # Use SharedCart method
                self.update_bash_script(package_name, add=True)
        else:
            if package_name in SharedCart.items:  # Use SharedCart instead of self.cart
                SharedCart.remove_item(package_name)  # Use SharedCart method
                self.update_bash_script(package_name, add=False)

        self.update_cart_display()
    
    def update_cart_display(self) -> None:
        cart_items = "\n".join(f"- {pkg}" for pkg in SharedCart.get_items())  # Use SharedCart method
        self.cart_display.update(f"Cart:\n{cart_items}")

    def update_bash_script(self, package_name: str, add: bool) -> None:
            # Retrieve the commands for the selected package
            package_steps = INSTALLATION_COMMANDS.get(package_name, [])

            if add:
                # Append the commands to the script
                with open(self.app.script_path, "a") as script_file:
                    for step in package_steps:
                        script_file.write(f"{step}\n")
            else:
                # Remove the package's commands from the script
                with open(self.app.script_path, "r") as script_file:
                    lines = script_file.readlines()
                with open(self.app.script_path, "w") as script_file:
                    skip = False
                    for line in lines:
                        if any(step in line for step in package_steps):
                            skip = True
                        elif skip and line.strip() == "":
                            skip = False
                        else:
                            script_file.write(line)

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
    
    def action_confirm_selection(self) -> None:
        self.app.selected_packages = self.cart  # Pass selected packages to the app
        self.app.show_confirmation_screen()
    
    def on_mount(self) -> None:
        """Called when the screen is mounted."""
        self.update_cart_display()

    def action_quit(self) -> None:
        self.app.exit()

    def action_go_back(self) -> None:
        self.app.pop_screen()
