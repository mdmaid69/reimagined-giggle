import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import os
def change_working_directory(path):
        os.chdir(path)