import os
def change_working_directory(path):
        os.chdir(path)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)