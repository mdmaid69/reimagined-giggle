import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)