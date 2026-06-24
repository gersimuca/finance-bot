import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from parser import process_file

processed = set()

def process_existing_files():
    for f in os.listdir("imports"):
        if f.endswith(".csv"):
            path = os.path.join("imports", f)
            if path not in processed:
                process_file(path)
                processed.add(path)

class Handler(FileSystemEventHandler):

    def on_created(self, event):
        if event.src_path.endswith(".csv"):
            if event.src_path not in processed:
                process_file(event.src_path)
                processed.add(event.src_path)

if __name__ == "__main__":

    os.makedirs("imports", exist_ok=True)

    print("Processing existing files...")
    process_existing_files()

    observer = Observer()
    observer.schedule(Handler(), "imports", recursive=False)

    observer.start()

    print("Watching imports/ for new CSV files...")

    while True:
        time.sleep(1)