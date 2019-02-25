
import os
from datetime import datetime

def readFile(filepath):
    output = ""
    with open(filepath) as file:
        for line in file:
            output+=line
        return output

def writeToFile(input,filepath):
    with open(filepath,"a") as file:
        file.write(input)

def generateFilename():
    current = datetime.now()
    timename = current.strftime("%Y-%m-%d-%H-%M-%S-%f")
    return timename+".txt"

filename = generateFilename()
for file in os.listdir("mydir"):
    if file.endswith(".txt"):
        output = readFile("mydir/%s"%file)
        print(output)
        writeToFile(output,filename)
