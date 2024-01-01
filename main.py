import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import os
def get_file_size(filename):
        return os.path.getsize(filename)