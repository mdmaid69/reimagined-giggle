import array
def get_array_as_float(array):
        return float(array[0])
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)