import math
def calculate_arc_cosine(x):
        return math.acos(x)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)