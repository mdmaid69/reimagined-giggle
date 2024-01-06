import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)