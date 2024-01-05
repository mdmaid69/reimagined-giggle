import math
def calculate_absolute_value(x):
        return math.fabs(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)