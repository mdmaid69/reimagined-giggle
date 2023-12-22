import array
def remove_from_array(array, item):
        array.remove(item)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)