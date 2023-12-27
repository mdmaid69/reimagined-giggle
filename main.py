import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)