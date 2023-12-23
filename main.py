import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)