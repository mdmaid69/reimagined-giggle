import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)