import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)