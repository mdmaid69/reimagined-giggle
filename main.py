import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a