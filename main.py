import array
def get_array_as_memoryview(array):
        return memoryview(array)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)