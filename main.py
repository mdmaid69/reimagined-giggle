import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable