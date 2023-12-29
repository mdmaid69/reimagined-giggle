import array
def iterate_over_array(array):
        for item in array:
        print(item)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)