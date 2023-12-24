import os
def change_working_directory(path):
        os.chdir(path)
import glob
def find_files(pattern):
        return glob.glob(pattern)