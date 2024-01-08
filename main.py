import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a