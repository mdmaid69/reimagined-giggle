import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)