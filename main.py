import sys
def add_to_python_path(path):
        sys.path.append(path)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a