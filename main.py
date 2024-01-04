import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height