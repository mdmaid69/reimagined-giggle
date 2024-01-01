import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a