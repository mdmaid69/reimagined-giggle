import os
def change_working_directory(path):
        os.chdir(path)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)