from textual.widgets import Static
from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Center
from installation_screen import InstallationScreen

class ConfirmationScreen(Screen):
    def __init__(self, selected_packages, script_path):
        super().__init__()
        self.selected_packages = selected_packages
        self.script_path = script_path

    BINDINGS = [
        ("enter", "confirm", "Confirm Installation"),
        ("escape", "go_back", "Back to Packages"),
        ("q", "quit", "Quit")
    ]

    CSS = """
    #confirm-title {
        text-align: center;
        text-style: bold;
        color: $success;
        margin: 1 0;
    }

    #package-list {
        margin: 1 0;
        padding: 1;
        border: round $primary;
    }

    #confirm-instructions {
        text-align: center;
        color: $warning;
        margin: 1 0;
    }

    #quit-instructions {
        text-align: center;
        color: $text;
        margin: 1 0;
    }
    """

    def compose(self) -> ComposeResult:
        with Center():
            yield Static("Selected Packages for Installation", id="confirm-title")
            yield Static("\n".join(f"- {pkg}" for pkg in self.selected_packages), id="package-list")
            yield Static("\nPress ENTER to confirm installation\nPress ESC to go back", id="confirm-instructions")  # Changed ID
            yield Static("Press 'q' to quit", id="quit-instructions")  # Changed ID

    def action_confirm(self) -> None:
        """Show the installation screen when Enter is pressed"""
        self.app.push_screen(InstallationScreen(self.script_path))

    def action_go_back(self) -> None:
        """Go back to previous screen when Escape is pressed"""
        self.app.pop_screen()

    def action_quit(self) -> None:
        """Quit the application"""
        self.app.exit()

    def run_script(self) -> None:
        import subprocess
        try:
            # Update status message
            self.query_one("#status-message").update("Installing packages... Please wait...")
            
            # Run the script
            subprocess.run(["bash", self.script_path], check=True)
            self.app.exit("Installation completed successfully!")
        except subprocess.CalledProcessError as e:
            self.app.exit(f"Error during installation: {e}")
        except FileNotFoundError:
            self.app.exit("Script not found. Please ensure the script exists.")