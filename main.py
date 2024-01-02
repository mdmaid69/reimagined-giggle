import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)