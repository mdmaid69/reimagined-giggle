import math
def calculate_logarithm_base_e(x):
        return math.log(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)