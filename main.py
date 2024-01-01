import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)