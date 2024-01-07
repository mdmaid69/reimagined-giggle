import array
def get_array_as_bytes(array):
        return bytes(array)
import os
def change_working_directory(path):
        os.chdir(path)