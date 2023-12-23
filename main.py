import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import array
def extend_array(array, iterable):
        array.extend(iterable)