import array
def get_array_as_memoryview(array):
        return memoryview(array)
import os
def remove_directory(path):
        os.rmdir(path)