import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)