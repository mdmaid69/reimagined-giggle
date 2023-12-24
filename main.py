import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)