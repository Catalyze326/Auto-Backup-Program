import errno
import os
import shutil
from shutil import copyfile
import time


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
        filelist.append(path)
        for f in files:
            filelist.append(path + "/" + f)
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
        filetime = (os.path.getmtime(x))
        if os.path.isdir(x) == False:
            if(realTime - filetime) > 300:
                copyfile(x, folderB + "/" + x)
        else:
                if os.path.isdir(folderB + "/" + x) == False:
                    os.mkdir(folderB + "/" + x)
                else:
                    print("Folder exists and therefore does not need to be created")
                continue


class main:
    folderA = getInitLoc()
    folderB = getFinLoc()

    try:
        while True:
            primary(folderA, folderB)
            time.sleep(300)
    except KeyboardInterrupt:
        primary(folderA, folderB)
        print("Goodbye World")

