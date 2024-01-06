import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)