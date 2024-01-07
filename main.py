import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def set_array_item(array, i, item):
        array[i] = item