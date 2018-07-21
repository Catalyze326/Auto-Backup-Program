import os
cont = 'y'
newProgram = open("main.py", "w")
newProgram.write("import os\n")


def getInitLoc():
    initLoc = input("Where would you like the files to move from?")
    return initLoc

def getFinLoc():
    finalLoc = input("Where would you like the files to go?")
    return finalLoc

while cont == 'y':
    newProgram.write("system.os(" + '"' +  "cp "  + getInitLoc() + " " + getFinLoc() + '"' + ")\n")
    cont = input("Would you like to add another folder? If yes answer Y if no answer N")
