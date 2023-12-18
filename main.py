import array
def get_array_item(array, i):
        return array[i]
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)