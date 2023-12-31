import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)