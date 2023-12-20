import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)