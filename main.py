import glob
def find_files(pattern):
        return glob.glob(pattern)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)