from os import listdir
import filecmp
import os
from shutil import copyfile

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
    return os.listdir(folderA)

def checkSame(fileA, fileB):
    return filecmp.cmp (fileA, fileB)

cont = 'y'
while cont == 'y':
    folderA = getInitLoc()
    folderB = getFinLoc()

    for x in listFolder(folderA):
        print(x)

    for x in listFolder(folderA):
        try:
            if checkSame(folderA + "/"+ x, folderB + "/"+ x) == True:
                needToChange.append(x)
        except FileNotFoundError:
            copyfile(folderA + "/"+ x, folderB)
        else:
            break

    cont = input("Would you like to add another folder? If yes answer Y if no answer N")

    for x in needToChange:
        copyfile(folderA + "/"+ x, folderB)
