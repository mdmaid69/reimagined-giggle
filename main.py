import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)