import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def get_array_item_count(array, item):
        return array.count(item)