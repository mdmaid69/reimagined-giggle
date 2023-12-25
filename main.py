import os
def get_environment_variable(var):
        return os.getenv(var)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable