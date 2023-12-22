import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def append_to_array(array, item):
        array.append(item)