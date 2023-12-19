import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)