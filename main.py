import math
def calculate_inverse_hyperbolic_sine(x):
        return math.asinh(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)