import math
def calculate_sign(x):
        return math.copysign(1, x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)