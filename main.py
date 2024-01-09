import array
def get_array_as_frozenset(array):
        return frozenset(array)
import os
def remove_directory(path):
        os.rmdir(path)