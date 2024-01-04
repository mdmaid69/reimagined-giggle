import os
def get_file_size(filename):
        return os.path.getsize(filename)
import glob
def find_files(pattern):
        return glob.glob(pattern)