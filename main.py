import os
def list_files_in_directory(path):
        return os.listdir(path)
import glob
def find_files(pattern):
        return glob.glob(pattern)