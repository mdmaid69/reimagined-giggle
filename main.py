import math
def calculate_factorial(n):
        return math.factorial(n)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)