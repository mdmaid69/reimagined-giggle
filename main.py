import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def iterate_over_array(array):
        for item in array:
        print(item)