import array
def get_array_as_tuple(array):
        return tuple(array)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)