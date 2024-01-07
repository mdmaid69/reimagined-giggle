import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable