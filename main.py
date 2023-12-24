import array
def get_array_as_bytes(array):
        return bytes(array)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)