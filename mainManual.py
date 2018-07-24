import filecmp
import os
from shutil import copyfile
import time
import glob

needToChange = ["deleteThis"]
del needToChange[0]


def getInitLoc():
    initLoc = input("Where would you like the files to move from?")
    return initLoc

def getFinLoc():
    finalLoc = input("Where would you like the files to go?")
    return finalLoc

def listFolder(folderA):
    # onlyfiles = [f for f in listdir(folderA) if isfile(join(FolderA, f))]
    for x in glob.iglob(folderA + "/*", recursive=True):

        #return filename

def checkSame(fileA, fileB):
    return filecmp.cmp (fileA, fileB)


def primary(folderA, folderB):

    for x in os.walk(folderA):
        try:
            if checkSame(folderA + "/"+ x, folderB + "/"+ x) == True:
                needToChange.append(x)
        except FileNotFoundError:
            print("Could not find file " + x + "in " + folderB + " putting it in " + folderB)
            copyfile(folderA + "/" + x, folderB + "/" + x)

    for x in needToChange:
        copyfile(folderA + "/"+ x, folderB + "/"+ x)

folderA = getInitLoc()
folderB = getFinLoc()

while True:
    primary(folderA, folderB)
    time.sleep(20)



