import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import os
def remove_directory(path):
        os.rmdir(path)