import array
def get_array_as_int(array):
        return int(array[0])
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)