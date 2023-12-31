import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import sys
def add_to_python_path(path):
        sys.path.append(path)