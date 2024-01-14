import subprocess
from SEDSS.CLIMessage import CLIMessage
import time

class GTBox_tmux:
    def __init__(self, session_name):
        self.session_name = session_name
        pass

    def startTmuxSession(self):
        try:
            subprocess.Popen(["xterm", "-e", f"tmux new-session -d -s {self.session_name} ; tmux attach -t {self.session_name}"])
            CLIMessage(f"Started tmux session '{self.session_name}' in a new xterm window.", "I")
        except Exception as e:
            CLIMessage(f"Error: {e}", "E")

    def sendCommandTmuxSession(self, command="sudo python main.py"):
        try:
            time.sleep (1)
            subprocess.Popen(["tmux", "send-keys", "-t", self.session_name, f"{command}", "C-m"])
            CLIMessage(f"Sent command '{command}' to tmux session '{self.session_name}'.", "I")
        except Exception as e:
            CLIMessage(f"Error: {e}", "E")

    def killTmuxSession(self):
        try:
            subprocess.run(["tmux", "kill-session", "-t", self.session_name])
            CLIMessage(f"Killed tmux session '{self.session_name}'.", "I")
        except Exception as e:
            CLIMessage(f"Error: {e}", "E")