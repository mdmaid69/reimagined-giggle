import sys
def add_to_python_path(path):
        sys.path.append(path)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)