import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import os
def get_file_size(filename):
        return os.path.getsize(filename)