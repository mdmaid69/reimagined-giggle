import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def get_array_slice(array, i, j):
        return array[i:j]