import array
def remove_from_array(array, item):
        array.remove(item)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)