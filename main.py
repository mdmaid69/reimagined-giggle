import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import math
def calculate_permutations(n, k):
        return math.perm(n, k)