import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)