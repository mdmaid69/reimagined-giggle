import math
def calculate_circle_area(radius):
        return math.pi * radius**2
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)