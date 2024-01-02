import array
def get_array_slice(array, i, j):
        return array[i:j]
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)