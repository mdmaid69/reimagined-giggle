import os
def list_files_in_directory(path):
        return os.listdir(path)
import array
def get_array_as_memoryview(array):
        return memoryview(array)