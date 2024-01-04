import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}