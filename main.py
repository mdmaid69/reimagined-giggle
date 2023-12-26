import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import array
def check_if_array_contains_item(array, item):
        return item in array