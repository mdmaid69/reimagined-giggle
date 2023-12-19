import os
def get_environment_variable(var):
        return os.getenv(var)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a