import math
def calculate_arc_tangent(x):
        return math.atan(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)