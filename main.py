import platform
def get_python_version():
        return platform.python_version()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)