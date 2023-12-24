import array
def get_array_as_float(array):
        return float(array[0])
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)