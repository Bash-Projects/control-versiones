# Start of Imports
# Watchdog imports: 
# pip install watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from shutil import copyfile

from datetime import datetime

import os
import json
import time
# End of imports

class BackupHandler(FileSystemEventHandler):
    def on_modified(self, event):
        i = 1
        now = datetime.now()
        
        print (event.src_path)
        # For every modified file in the modified directory TODO limit this to ONLY the file in question
        for filename in os.listdir(event.src_path):
            print("Backing Up: " + filename)
            # Check if filename is in blacklist
            skip = False
            if not filename in black_list:
                for f in black_list:
                    if filename.startswith(f):
                        skip = True
            else:
                skip = True

            # Is it a directory or present in blacklist?
            if not os.path.isdir(tracked_folder + "/" + filename) and not skip:
                # We're going to create a new file to store the backup files in (collate them all together)
                new_destination_folder = destination_folder + "/" + filename.split("1")[0]
                # Check folder exists, if not create it
                if not os.path.isdir(new_destination_folder):
                    os.mkdir(new_destination_folder, access_rights)

                # Now reformat the filename to include datetime
                new_name = now.strftime(dt_format) + "_" + filename
                # Now check the filename doesn't already exist - if it does add an integer
                file_exists = os.path.isfile(destination_folder + "/" + new_name)
                while file_exists:
                    self.i += 1
                    new_name = i + new_name
                    file_exists = os.path.isfile(destination_folder + "/" + new_name)


                # Actually store it now
                src = event.src_path + "/" + filename
                destination = new_destination_folder + "/" + new_name
                copyfile(src, destination)

# Clear terminal
os.system("clear")
# define the access rights to make a folder
access_rights = 0o755
# Date time format to append to filename
dt_format = "%d-%m-%Y %H.%M.%S"
# Which folder are we watching?
tracked_folder = "/Users/matthew/Documents"
# Which folder are we backing up the files to?
destination_folder = "/Users/matthew/Desktop/backups"

#black listed files 
black_list = [
    ".DS_Store", # For Mac's OS specifically
]


# Setup the observer and run
event_handler = BackupHandler()
observer = Observer()
observer.schedule(event_handler, tracked_folder, recursive=True)
observer.start()

# Run indefinitely unless stopped by user
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()