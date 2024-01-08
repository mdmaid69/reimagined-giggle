import array
def set_array_item(array, i, item):
        array[i] = item
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)