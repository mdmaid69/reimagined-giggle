import array
def get_array_as_set(array):
        return set(array)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)