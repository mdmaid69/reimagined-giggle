import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import os
def get_environment_variable(var):
        return os.getenv(var)