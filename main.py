import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a