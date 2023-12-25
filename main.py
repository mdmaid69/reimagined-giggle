import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a