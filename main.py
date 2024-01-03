import platform
def get_python_version():
        return platform.python_version()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}