import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/lilydalmia/Downloads"           
to_dir = "/Users/lilydalmia/Downloads"



class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("A file has been created!: ",(event.src_path))
    def on_modified(self, event):
        print("A file has been modified!",(event.src_path))
    def on_moved(self, event):
        print("A file has been moved!",(event.src_path))
    def on_deleted(self, event):
        print("A file has been deleted!",(event.src_path))


event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
