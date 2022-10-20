import os
import sys
import shutil
from pathlib import Path
import time
import glob

print("Mass folder creator\n ")

while True:
    folderPath = input("Paste or type the folder path: ")
    if "\\" not in folderPath:
        print("This is not a folder path! Try again.")
    else:
        break

fileExtension = input("Type the file extension you want to make folders of (i.e .txt): ")

filelist = os.listdir(folderPath)

if len(filelist) == 0:
    print("There are no files of that type in that folder. Quitting..")
    sys.exit(0)

if len(filelist) > 0:
    fileNumber = 0
    typedList = []  # creating an empty list to store the filenames with the desired extension
    for file in filelist:
        if file.endswith(fileExtension):
            fileNumber = fileNumber + 1
            typedList.append(file)
    print("There are " + str(fileNumber) + " file(s) in the folder.")

    answer = input("Do you want to proceed? y/n: ")

    if answer.lower().startswith("y"):
        rootDir = folderPath
        keepExt = fileExtension
        searchPath = Path(rootDir)

        for file in searchPath.rglob("*"):
            if file.name.endswith(keepExt):
                print(file)
                name = (os.path.splitext(file.name)[0])
                newFolder = os.path.join(rootDir, name)
                if not os.path.exists(newFolder):
                    os.mkdir(newFolder)
                    print("Made File Directory: " + newFolder)
                    destination = os.path.join(newFolder, name) + fileExtension
                    shutil.move(file, destination)

    elif answer.lower().startswith("n"):
        print("Bye!")
        sys.exit(0)

    else:
        print("Wrong answer, please restart the script!")
        time.sleep(2)
        quit()
