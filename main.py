import os
def get_environment_variable(var):
        return os.getenv(var)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a