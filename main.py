import array
def get_array_length(array):
        return len(array)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)