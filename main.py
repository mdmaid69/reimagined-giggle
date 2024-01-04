import array
def get_array_as_set(array):
        return set(array)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)