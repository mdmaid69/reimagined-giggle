import array
def get_array_as_bytes(array):
        return bytes(array)
import os
def get_file_size(filename):
        return os.path.getsize(filename)