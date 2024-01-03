import os
def get_file_size(filename):
        return os.path.getsize(filename)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)