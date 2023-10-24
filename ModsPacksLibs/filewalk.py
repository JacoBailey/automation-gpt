import os

def filewalk(directory): #TODO: Determine way to hide hidden filetypes such as .DS_Store
    for root, dirs, files in os.walk(directory):
        directoryFiles = files
    return directoryFiles
