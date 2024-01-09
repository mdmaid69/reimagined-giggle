import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)