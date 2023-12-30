import math
def calculate_tangent(x):
        return math.tan(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)