import os
def get_file_size(filename):
        return os.path.getsize(filename)
import array
def extend_array(array, iterable):
        array.extend(iterable)