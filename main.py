import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius