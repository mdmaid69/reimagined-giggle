import sys
def add_to_python_path(path):
        sys.path.append(path)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)