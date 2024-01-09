import math
def calculate_square_root(x):
        return math.sqrt(x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a