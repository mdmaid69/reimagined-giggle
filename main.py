import os
def get_file_size(filename):
        return os.path.getsize(filename)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)