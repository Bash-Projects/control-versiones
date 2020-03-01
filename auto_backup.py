# Start of Imports
# Watchdog imports: 
# pip install watchdog
from watchgod import watch

from shutil import copyfile

from datetime import datetime

import ntpath

import os
import json
import time
import sys
# End of imports

# Colours for use in terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Clear terminal
os.system("clear")
# define the access rights to make a folder
access_rights = 0o755
# Date time format to append to filename
dt_format = "-%y%m%d-%H:%M:%S"
# Which folder are we watching?
tracked_folder = ""
# Which folder are we backing up the files to?
destination_folder = ""

# Perform setup checks
# Check a destination folder has been provided
if destination_folder == "":
    print(f"{bcolors.FAIL}Please define a destination folder (Where to save backups to)")
    exit()
else:
    print (f"{bcolors.ENDC}Escuchando los cambios en: ", destination_folder)


# Check a folder to track has been provided
if tracked_folder == "":
    print(f"{bcolors.FAIL}Please define a folder to track")
    exit()
else:
    # Check it exists
    if not os.path.isdir(tracked_folder):
        print (f"{bcolors.FAIL}Destination provided is either not a directory or does not exist. Please try again")
        exit()

# Check the destination directory actually exists, if not, create it
if not os.path.isdir(destination_folder):
    print (f"{bcolors.ENDC}Backup directory not created. Creating directory....")
    os.mkdir(destination_folder, access_rights)

# End of setup checks

# Start listening for changes
# Loop through each individual change
for changes in watch(tracked_folder):
    i = 0
    now = datetime.now()
    # Each change in the set
    for change in changes:
        # Remove filename and path from the array
        file = change[1]

        # Get filename from path
        filename = ntpath.basename(file)
        print (f"{bcolors.ENDC}Backing up file: ", filename)

        new_dir = destination_folder + filename

        if not os.path.isdir(new_dir):
            print (f"{bcolors.ENDC}New file detected, creating directory....")
            os.mkdir(new_dir, access_rights)

        # Now reformat the filename to include datetime
        new_name = now.strftime(dt_format) + "_" + filename
        # Now check the filename doesn't already exist - if it does add an integer
        file_exists = os.path.isfile(destination_folder + "/" + new_name)
        while file_exists:
            i += 1
            new_name = i + new_name
            file_exists = os.path.isfile(destination_folder + new_name)

        # Actually store it now
        try :
            destination = new_dir + new_name
            copyfile(file, destination)
        except FileNotFoundError as err:
            print (f"{bcolors.FAIL}File not found exception occurred: {0}".format(err))
        except : 
            print (f"{bcolors.FAIL}An unknown exception occurred", sys.exc_info()[0])
