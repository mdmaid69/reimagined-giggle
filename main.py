import sys
def print_python_version():
        print(sys.version)
import array
def get_array_as_memoryview(array):
        return memoryview(array)