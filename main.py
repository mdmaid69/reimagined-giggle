import glob
def find_files(pattern):
        return glob.glob(pattern)
import os
def remove_directory(path):
        os.rmdir(path)