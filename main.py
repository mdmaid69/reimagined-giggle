import math
def calculate_tangent(x):
        return math.tan(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a