import math
def calculate_sine(x):
        return math.sin(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)