import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)