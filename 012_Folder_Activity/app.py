# =============================================
#  Entry Level ID
# =============================================

import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import init, Fore, Style

# Inisialisasi Colorama
init(autoreset=True)

# Set folder yang akan dimonitor
folder_to_watch = r"C:\Users\Xbravo\Downloads"

# Set up logging ke file dan terminal
logger = logging.getLogger("folder_monitor")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler("folder_activity_log.txt")
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)

# Tambahkan handler ke logger
logger.addHandler(file_handler)

class FolderActivityHandler(FileSystemEventHandler):
    def on_created(self, event):
        message = f"File created: {event.src_path}"
        print(Fore.GREEN + message)
        logger.info(message)

    def on_modified(self, event):
        message = f"File modified: {event.src_path}"
        print(Fore.YELLOW + message)
        logger.info(message)

    def on_deleted(self, event):
        message = f"File deleted: {event.src_path}"
        print(Fore.RED + message)
        logger.info(message)

    def on_moved(self, event):
        message = f"File moved: from {event.src_path} to {event.dest_path}"
        print(Fore.CYAN + message)
        logger.info(message)

if __name__ == "__main__":
    print(Fore.MAGENTA + f"Monitoring folder: {folder_to_watch} ... Press Ctrl+C to stop.")
    
    event_handler = FolderActivityHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
