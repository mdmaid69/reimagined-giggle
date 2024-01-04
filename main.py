import os
def get_environment_variable(var):
        return os.getenv(var)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)