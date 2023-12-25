import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)