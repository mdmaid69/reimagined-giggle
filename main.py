import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))