import time
import subprocess
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 🔹 Path to your local repo
repo_path = "C:\Automate-Github"

class GitAutoPushHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"Detected change in: {event.src_path}")
            commit_message = f"Auto update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            commands = [
                "git add .",
                f'git commit -m "{commit_message}"',
                "git push origin main"
            ]
            for cmd in commands:
                subprocess.run(cmd, shell=True, cwd=repo_path)

if __name__ == "__main__":
    event_handler = GitAutoPushHandler()
    observer = Observer()
    observer.schedule(event_handler, repo_path, recursive=True)
    observer.start()
    print("🔄 Watching for changes... Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
