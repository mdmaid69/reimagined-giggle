import array
def iterate_over_array(array):
        for item in array:
        print(item)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)