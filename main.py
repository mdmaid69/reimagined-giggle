import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import glob
def find_files(pattern):
        return glob.glob(pattern)