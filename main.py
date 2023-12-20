import array
def get_array_item(array, i):
        return array[i]
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)