from textual.app import App, ComposeResult
from textual.widgets import Header, Input, Footer, Markdown, Button, Label, Static
from textual.containers import VerticalScroll, Center
from textual.screen import Screen
from distro import DistroOption, DistroSelectScreen

class WelcomeScreen(Screen):

    BINDINGS = [
        ("n", "distro_select", "Next Screen"),
        ("q", "quit", "Quit")
    ]
    
    def action_quit(self) -> None:
        self.app.exit()

    def action_distro_select(self) -> None:
        self.app.push_screen("distro_select")
    
    def compose(self) -> ComposeResult:
        
        with Center():
            yield Label("Linux Starter Pack", id="title")
            yield Label("A quick way to install packages in your Linux system", id="subtitle")
        
        yield Footer()

class App(App):
    
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
        self.push_screen("welcome")


if __name__ == "__main__":
    App().run()             