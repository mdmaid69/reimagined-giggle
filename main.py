import array
def get_array_typecode(array):
        return array.typecode
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)