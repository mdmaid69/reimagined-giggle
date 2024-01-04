import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import sys
def add_to_python_path(path):
        sys.path.append(path)