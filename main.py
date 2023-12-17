import array
def convert_array_to_list(array):
        return array.tolist()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)