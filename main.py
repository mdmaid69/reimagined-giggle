import array
def get_array_index(array, item):
        return array.index(item)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)