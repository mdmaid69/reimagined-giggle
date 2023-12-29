import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array