import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)