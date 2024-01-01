import array
def get_array_as_memoryview(array):
        return memoryview(array)
import os
def get_environment_variable(var):
        return os.getenv(var)