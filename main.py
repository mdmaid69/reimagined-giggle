import os
def get_current_working_directory():
        return os.getcwd()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}