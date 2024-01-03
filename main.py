import array
def get_array_as_bool(array):
        return bool(array)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)