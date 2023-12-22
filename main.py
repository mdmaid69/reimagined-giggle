import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)