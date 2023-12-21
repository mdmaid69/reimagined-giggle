import os
def get_environment_variable(var):
        return os.getenv(var)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)