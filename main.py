import array
def get_array_as_frozenset(array):
        return frozenset(array)
import os
def get_environment_variable(var):
        return os.getenv(var)