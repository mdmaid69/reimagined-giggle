import array
def get_string_from_array(array):
        return array.tobytes()
import os
def get_environment_variable(var):
        return os.getenv(var)