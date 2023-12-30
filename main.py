import array
def append_to_array(array, item):
        array.append(item)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)