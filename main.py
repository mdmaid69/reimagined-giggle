import sys
def print_python_version():
        print(sys.version)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)