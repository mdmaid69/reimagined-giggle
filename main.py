import array
def get_array_buffer_info(array):
        return array.buffer_info()
import os
def get_environment_variable(var):
        return os.getenv(var)