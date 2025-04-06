from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Log, ProgressBar
from textual.containers import ScrollableContainer
from textual.message import Message
import subprocess
import threading

class InstallationScreen(Screen):
    """Screen that shows the installation progress"""

    CSS = """
    #installation-title {
        text-align: center;
        text-style: bold;
        color: $success;
        margin: 1 0;
    }

    #installation-log {
        height: 85%;  /* Reduced to make room for progress bar */
        border: round $primary;
        padding: 1;
        margin: 1;
        background: $surface;
        color: $text;
    }

    #progress-bar {
        height: auto;
        margin: 1;
        max-width: 5fr;
    }

    #status-message {
        text-align: center;
        color: $warning;
        margin: 1 0;
    }
    """

    class LogOutput(Message):
        """Custom message for log output"""
        def __init__(self, output: str):
            super().__init__()
            self.output = output

    def __init__(self, script_path: str):
        super().__init__()
        self.script_path = script_path
        self.installation_complete = False
        self.total_commands = self._count_commands()
        self.current_command = 0

    def _count_commands(self) -> int:
        """Count the total number of commands in the installation script"""
        try:
            with open(self.script_path, 'r') as f:
                # Count non-empty lines that don't start with # or echo
                return sum(1 for line in f if line.strip() 
                         and not line.strip().startswith('#') 
                         and not line.strip().startswith('echo'))
        except Exception:
            return 0

    def compose(self) -> ComposeResult:
        yield Static("Installing Packages...", id="installation-title")
        yield Log(id="installation-log")
        yield ProgressBar(total=100, id="progress-bar")
        yield Static("Installation in progress... Press Q to quit", id="status-message")

    BINDINGS = [
        ("q", "quit", "Quit")
    ]

    def on_mount(self) -> None:
        """Start the installation when the screen is mounted"""
        self.log_widget = self.query_one("#installation-log")
        threading.Thread(target=self.run_installation, daemon=True).start()

    def update_progress(self) -> None:
        """Update the progress bar"""
        if self.total_commands > 0:
            progress = (self.current_command / self.total_commands) * 100
            self.query_one("#progress-bar").update(progress=progress)

    def run_installation(self) -> None:
        """Run the installation script and capture output"""
        try:
            process = subprocess.Popen(
                ["bash", self.script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )

            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    self.post_message(self.LogOutput(output.strip()))
                    # Update progress when command completes (look for sudo or common commands)
                    if any(cmd in output.lower() for cmd in ['apt', 'dnf', 'pacman','zypper','nix-env', 'installed', 'complete']):
                        self.current_command += 1
                        self.update_progress()

            return_code = process.poll()
            
            # Ensure progress bar reaches 100% on successful completion
            if return_code == 0:
                self.query_one("#progress-bar").update(progress=100)
                self.post_message(self.LogOutput("\n✅ Installation completed successfully!"))
            else:
                self.post_message(self.LogOutput(f"\n❌ Installation failed with return code {return_code}"))

        except Exception as e:
            self.post_message(self.LogOutput(f"\n❌ Error during installation: {str(e)}"))

        self.installation_complete = True
        self.query_one("#status-message").update("Installation complete. Press Q to quit")

    def on_installation_screen_log_output(self, message: LogOutput) -> None:
        """Handle log output messages"""
        self.log_widget.write_line(message.output)  # Changed to write_line for better formatting

    def action_quit(self) -> None:
        """Quit the application"""
        if self.installation_complete:
            self.app.exit()
        else:
            self.query_one("#status-message").update("Installation in progress... Please wait.")