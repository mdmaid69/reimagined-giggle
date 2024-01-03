import array
def convert_array_to_string(array):
        return array.tostring()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)