import array
def get_array_as_tuple(array):
        return tuple(array)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)