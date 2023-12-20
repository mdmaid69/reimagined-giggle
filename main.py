import array
def remove_from_array(array, item):
        array.remove(item)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)