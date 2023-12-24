import os
def change_working_directory(path):
        os.chdir(path)
import array
def get_array_as_frozenset(array):
        return frozenset(array)