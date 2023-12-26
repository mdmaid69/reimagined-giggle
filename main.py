import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)