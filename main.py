import array
def get_array_as_bytearray(array):
        return bytearray(array)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)