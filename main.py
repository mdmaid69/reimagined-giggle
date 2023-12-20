import sys
def add_to_python_path(path):
        sys.path.append(path)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable