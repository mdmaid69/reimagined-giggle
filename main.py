import array
def get_array_as_bytearray(array):
        return bytearray(array)
import os
def change_working_directory(path):
        os.chdir(path)