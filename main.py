import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)