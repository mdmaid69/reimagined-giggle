import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import re
def split_string(pattern, string):
        return re.split(pattern, string)