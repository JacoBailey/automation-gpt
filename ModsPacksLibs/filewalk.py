import os

class invalidDirectory(Exception):
    'Invalid directory provided. Please provide a valid directory.'
    pass

def filewalk(directory): #TODO: Determine way to hide hidden filetypes such as .DS_Store
    try:
        for root, dirs, files in os.walk(directory):
            directoryFiles = files
        return directoryFiles
    except UnboundLocalError:
        raise invalidDirectory