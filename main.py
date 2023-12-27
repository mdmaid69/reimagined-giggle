import array
def extend_array(array, iterable):
        array.extend(iterable)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)