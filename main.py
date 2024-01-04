import sys
def print_python_version():
        print(sys.version)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)