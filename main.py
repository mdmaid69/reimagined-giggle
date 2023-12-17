import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)