import os
def get_file_size(filename):
        return os.path.getsize(filename)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}