import array
def get_array_as_int(array):
        return int(array[0])
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)