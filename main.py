import array
def get_array_index(array, item):
        return array.index(item)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)