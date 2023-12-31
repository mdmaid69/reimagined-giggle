import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)