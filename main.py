import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)