import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)