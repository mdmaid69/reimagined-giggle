import array
def get_array_slice(array, i, j):
        return array[i:j]
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)