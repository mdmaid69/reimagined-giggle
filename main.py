import os
def list_files_in_directory(path):
        return os.listdir(path)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)