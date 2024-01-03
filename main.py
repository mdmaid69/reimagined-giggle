import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)