def reverse_string(s):
        return s[::-1]
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)