import array
def get_array_as_bool(array):
        return bool(array)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)