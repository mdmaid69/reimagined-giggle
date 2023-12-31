import os
def list_files_in_directory(path):
        return os.listdir(path)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)