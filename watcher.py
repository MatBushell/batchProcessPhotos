import subprocess
import os
import time
import glob
import json
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

photoshop_path = r"C:\Program Files\Adobe\Adobe Photoshop 2025\Photoshop.exe"
intake_folder = r"D:\Photos\sony_a6000\intake"
arw_archive = r"D:\photos\sony_a6000\raw_archive"
processed_jpegs = r"D:\photos\sony_a6000\processed_jpegs"

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        # called when any files is created
        if not event.is_directory and event.src_path.endswith('.ARW'):
            print(f'New files detected: {event.src_path}')
            # Trigger your processing here
            process_files()

def process_files():
    # Get fresh date each time this runs
    current_date = datetime.now().strftime("%B_%d_%Y")  # "December_04_2025"
    # Get files
    arw_files = glob.glob(os.path.join(intake_folder,"*.ARW"))
    # create date specific folders
    jpeg_output = os.path.join(processed_jpegs, current_date)
    arw_output = os.path.join(arw_archive, current_date)

    if len(arw_files) == 0:
        print("No ARW files found in intake folder")

    with open("queue.json", "w") as f:
        json.dump({
            "files": arw_files,
            "output_folder": current_date
            }, f)

    try:
        process = subprocess.Popen([photoshop_path])
        print('Opening Photoshop...')

    except FileNotFoundError:
        print(f'Error: Could not find Photoshop at {photoshop_path}')
        print('Please check the path and try again.')

# Set up the watcher
observer = Observer()
handler = FileHandler()
observer.schedule(handler, path=intake_folder, recursive=False)
observer.start()

print(f'Watching {intake_folder} for new ARW files...')

try:
    while True:
        time.sleep(1) # keep script running
except KeyboardInterrupt:
    observer.stop()
    print('Stopped watching')

observer.join()


