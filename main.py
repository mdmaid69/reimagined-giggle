import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def get_array_item_count(array, item):
        return array.count(item)