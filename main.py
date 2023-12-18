import array
def get_array_as_bytearray(array):
        return bytearray(array)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)