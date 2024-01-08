import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import os
def list_files_in_directory(path):
        return os.listdir(path)