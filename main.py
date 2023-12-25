import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)