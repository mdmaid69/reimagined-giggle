import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a