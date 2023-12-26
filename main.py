import array
def clear_array(array):
        array *= 0
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)