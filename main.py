import errno
import os
import shutil
from shutil import copyfile
import time

# change it so that it reads from a file that has the paths of the src and dst folders and then it can do a dozen folders and change all the time and have no isstue
from typing import Any, Union


def getInitLoc():
    initLoc = input("Where would you like the files to move from?")
    return initLoc


def getFinLoc():
    finalLoc = input("Where would you like the files to go?")
    return finalLoc


def listFolder(folderA):
    return os.listdir(folderA)


def listFiles(path):
    filelist = []
    for path, dirs, files in os.walk(path):
        # filelist.append(path)
        for f in files:
            filelist.append(f)
    return filelist


def copytree(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise


def primary(folderA, folderB):
    files = listFiles(folderA)
    realTime = (time.time())

    for x in files:
        print(x)
        if os.path.exists(x):
            filetime = (os.path.getmtime(x))
        else:
            copyfile(x, folderB + "/" + x)
        if not os.path.isdir(x):
            if(realTime - filetime) > 20:
                copyfile(x, folderB + "/" + x)
        else:
                if not os.path.isdir(folderB + x):
                    os.mkdir(folderB + "/" + x)
                else:
                    print("Folder exists and therefore does not need to be created")
                continue


class main:
    folderA = "/mnt/c/Users/caleb/Documents/GitHub/moveFilesAuto/A"
    folderB = "/mnt/f/backupProgram"

    try:
        while True:
            primary(folderA, folderB)
            time.sleep(20)
    except KeyboardInterrupt:
        primary(folderA, folderB)
        print("Goodbye World")

