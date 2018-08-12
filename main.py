import os
import time
from shutil import copy

#Does most of the work.
def primary(src, dst):
    # Make file tree
    if not os.path.exists(dst):
        os.mkdir(dst)
    if not os.path.exists(dst + "\\" + src):
        os.mkdir(dst + "\\" + src)

    for x in listDirs(src):
        # print(dst + "\\" + x)
        if not os.path.exists(dst + "\\" + x):
            os.mkdir(dst + "\\" + x)

    # Does the oraginal file transfer some reason you have to do xcopy
    # if you want to do recursive copying because windows sucks also the /E dictates that it is recursive.
    # For some reason the people at microsoft decided that -R was not okay for recursive.
    for x in listFiles(src):
        if os.path.exists(x):
            # print(x)
            copy(x, dst + "\\" + x)

    # time.time() Gets the exact time in seconds using Unix Epoch Time what this means is that it gets the exact amount of seconds to many decimal places since Jan 1, 1970 00:00:00
    # os.path.getmtime(x) is the time that the file was last edited with the same format of an answer.
    # I use these two numbers to check if any of the files need to be transferred because they have been edited in the last 5 min. Any other files do not need to be transferred.
    for x in listFiles(src):
        if (os.path.getmtime(x) + 300) > time.time():
            # print(dst + "\\" + x)
            copy(x, dst + "\\" + x)


def listFiles(loc):
    filelist = []
    for path, dirs, files in os.walk(loc):
        for d in dirs:
            print(path + "\\" + d)
        for f in files:
            lol = (path + "\\" + f)
            filelist.append(lol)
    return filelist


def listDirs(loc):
    dirlist = []
    for path, dirs, files in os.walk(loc):
        for d in dirs:
            lol = (path + "\\" + d)
            dirlist.append(lol)
    return dirlist


# This is how I worked around having many src and dst files.
# I have it written such that every other time the for loop runs it creates the src var
# and the other time it creates the dst var and then after it is done it calls primary.
def main():
    counter = 0
    for x in locations:
        if counter % 2 == 0:
            src = x
            print(x)
        else:
            dst = x
            print(x)
            primary(src, dst)
        counter = counter + 1
    print(counter)


try:
    # Initial creation of the file that holds the src and dst locations
    if not os.path.exists("inputs.txt"):
        file = open("inputs.txt", "w")
        cont = "y"
        while cont[0].lower() == "y":
            print("When giving an input do not put as \\ at the end of the source or destanation")
            file.write(input("Where is the initial file location?\n") + "\n")
            file.write(input("Where is the final file location?\n") + "\n")
            cont = input("Would you like to put in another set of locations.\n")
        file.close()

    while True:
        # take apart the text file line by line
        with open("inputs.txt") as f:
            locations = f.readlines()
        # remove whitespace characters like `\n` at the end of each line
        locations = [x.strip() for x in locations]
        main()
        # Runs every 5 min
        time.sleep(300)
# If the program is killed than it will run again to back everything up one last time
except KeyboardInterrupt:
    main()