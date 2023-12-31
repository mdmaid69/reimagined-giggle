import array
def get_array_typecode(array):
        return array.typecode
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)