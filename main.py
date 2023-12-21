import array
def get_array_as_memoryview(array):
        return memoryview(array)
import sys
def add_to_python_path(path):
        sys.path.append(path)