import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def extend_array(array, iterable):
        array.extend(iterable)