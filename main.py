import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import os
def get_environment_variable(var):
        return os.getenv(var)