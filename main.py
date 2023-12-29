import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)