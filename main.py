import os
def get_file_size(filename):
        return os.path.getsize(filename)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)