import array
def get_array_as_memoryview(array):
        return memoryview(array)
import os
def get_file_size(filename):
        return os.path.getsize(filename)