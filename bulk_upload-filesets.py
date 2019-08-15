import subprocess
import platform
import sys
import os
from glob import glob
from __builtin__ import raw_input

## TO hard code variables
server = "MY.SERVER.ORG"
username = "fwadmin"
password = "filewave"
fileset_path = "~/Documents/My Filesets"
fileset_group = "imported"

# Prompt user for variables if empty
if server == '':
    server = raw_input("Server FQDN: ")

if username == '':
    username = raw_input("username: ")

if password == '':
    password = raw_input("password: ")

if fileset_path == '':
    fileset_path = raw_input("Provide path to a folder of filesets: ")

# Detect OS
if platform.system() == "Darwin":
    print ("macOS / Darwin Detected")
    adminpath = "/Applications/FileWave/FileWave Admin.app/Contents/MacOS/FileWave Admin"
elif platform.system() == "Windows":
    print ("Redmond Winder OS Detected")
    adminpath = "FileWave Admin"
elif platform.system() == "Linux":
    print ("Nix Detected")
    adminpath = "FileWave Admin"
else:
    sys.exit("OS detection error. Aborting")

print(adminpath)
print(fileset_path)
print("################################################################################")
print("#                               Starting Upload                                #")
print("################################################################################")

for dirs in os.walk(fileset_path):
    for x in glob(os.path.join(dirs[0], '*.fileset')):
        fileset_group = os.path.basename(os.path.dirname((x)))
        print("Uploading: ", os.path.basename(x), " to ", fileset_group)
        subprocess.check_output(
            [adminpath,
             "-H", server,
             "-u", username,
             "-p", password,
             "--importFileset", x,
             "--filesetgroup", fileset_group]
        ),

print("################################################################################")
print("#                                 Done Upload                                  #")
print("################################################################################")
