import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a