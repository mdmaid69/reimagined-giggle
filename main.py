import math
def calculate_ceiling(x):
        return math.ceil(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)