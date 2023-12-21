import os
def change_working_directory(path):
        os.chdir(path)
import array
def get_array_as_memoryview(array):
        return memoryview(array)