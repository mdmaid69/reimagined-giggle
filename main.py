import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)