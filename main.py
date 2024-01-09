import platform
def get_python_version():
        return platform.python_version()
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable