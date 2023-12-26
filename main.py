import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import sys
def add_to_python_path(path):
        sys.path.append(path)