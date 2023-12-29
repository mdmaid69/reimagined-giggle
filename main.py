import platform
def get_python_version():
        return platform.python_version()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)