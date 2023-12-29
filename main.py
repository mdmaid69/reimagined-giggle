import sys
def add_to_python_path(path):
        sys.path.append(path)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a