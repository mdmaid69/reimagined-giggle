import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)