import os
from pathlib import Path

class InvalidDirectoryError(Exception):
    """Raised when an invalid directory is provided."""
    pass

class SimpleDirWalk:
    def __init__(self, directory):
        if not Path(directory).is_dir():
            raise InvalidDirectoryError('Invalid directory provided. Please provide a valid directory.')
        for root, dirs, files in os.walk(directory):
            self.root = root
            self.dirs = dirs
            self.files = files
            break