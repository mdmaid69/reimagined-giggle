import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)