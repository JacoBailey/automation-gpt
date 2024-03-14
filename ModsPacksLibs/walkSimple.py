import os

class invalidDirectory(Exception):
    'Invalid directory provided. Please provide a valid directory.'
    pass

class walk_simple:
    def __init__(self, directory):
        if os.path.exists(directory) == False:
            raise invalidDirectory
        self.root = ''
        self.dirs = ''
        self.files = ''
        for root, dirs, files in os.walk(directory):
            self.root = root
            self.dirs = dirs
            self.files = files