import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def check_if_array_contains_item(array, item):
        return item in array