import math
def calculate_square_root(x):
        return math.sqrt(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a