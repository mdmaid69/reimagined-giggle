import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import math
def calculate_hyperbolic_sine(x):
        return math.sinh(x)