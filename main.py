import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import array
def get_array_as_memoryview(array):
        return memoryview(array)