import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)