from GTBox_tmux import GTBox_tmux
from SEDSS.CLIMessage import CLIMessage

import time

def main():
	session_name = "Test"
	tmux = GTBox_tmux(session_name)
	try:
		tmux.startTmuxSession()
		CLIMessage("Session started. Press Ctrl+C to exit.", "W")
		tmux.sendCommandTmuxSession()
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		CLIMessage("\nCtrl+C pressed. Killing the tmux session...", "W")
		tmux.killTmuxSession()
		CLIMessage("Session killed. Exiting.")

if __name__ == "__main__":
	main()
