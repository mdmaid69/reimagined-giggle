import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)