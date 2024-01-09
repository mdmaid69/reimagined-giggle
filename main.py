import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)