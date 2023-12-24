import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)