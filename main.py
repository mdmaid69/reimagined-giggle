import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a