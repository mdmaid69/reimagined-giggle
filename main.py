import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)