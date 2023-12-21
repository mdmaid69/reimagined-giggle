import glob
def find_files(pattern):
        return glob.glob(pattern)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)