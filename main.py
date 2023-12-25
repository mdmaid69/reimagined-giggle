import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))