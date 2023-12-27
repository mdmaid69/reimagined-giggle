import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a