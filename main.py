import os
def get_file_size(filename):
        return os.path.getsize(filename)
import array
def get_array_item_count(array, item):
        return array.count(item)