import array
def get_array_as_bytearray(array):
        return bytearray(array)
import os
def get_environment_variable(var):
        return os.getenv(var)