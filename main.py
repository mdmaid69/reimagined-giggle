import sys
def print_python_version():
        print(sys.version)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)