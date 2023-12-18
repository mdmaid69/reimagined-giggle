import os
def get_environment_variable(var):
        return os.getenv(var)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)