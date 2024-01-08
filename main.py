import math
def calculate_ceiling(x):
        return math.ceil(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a