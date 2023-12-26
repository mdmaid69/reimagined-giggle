import sys
def print_python_version():
        return sys.version
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}