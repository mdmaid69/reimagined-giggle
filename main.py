import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable