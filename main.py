import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)