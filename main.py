import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import os
def list_files_in_directory(path):
        return os.listdir(path)