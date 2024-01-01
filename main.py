import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def check_if_array_contains_item(array, item):
        return item in array