import os
def remove_directory(path):
        os.rmdir(path)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)