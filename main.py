import array
def convert_array_to_bytes(array):
        return array.tobytes()
import os
def get_environment_variable(var):
        return os.getenv(var)