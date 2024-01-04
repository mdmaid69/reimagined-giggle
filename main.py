import glob
def find_files(pattern):
        return glob.glob(pattern)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)