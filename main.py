import array
def get_array_item_count(array, item):
        return array.count(item)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)