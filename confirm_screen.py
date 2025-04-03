from textual.widgets import Button, Static
from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import VerticalScroll
from textual.reactive import reactive

class ConfirmationScreen(Screen):
    def __init__(self, selected_packages, script_path):
        super().__init__()
        self.selected_packages = selected_packages
        self.script_path = script_path

    def compose(self) -> ComposeResult:
        yield Static("Confirm Installation", id="confirm-title")
        yield Static("\n".join(self.selected_packages), id="package-list")
        yield Button("Confirm", id="confirm-button")
        yield Button("Go Back", id="back-button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "confirm-button":
            self.run_script()
        elif event.button.id == "back-button":
            self.app.pop_screen()

    def run_script(self) -> None:
        import subprocess
        try:
            subprocess.run(["bash", self.script_path], check=True)
            self.app.exit("Installation completed successfully!")
        except subprocess.CalledProcessError as e:
            self.app.exit(f"Error during installation: {e}")
        except FileNotFoundError:
            self.app.exit("Script not found. Please ensure the script exists.")