import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)