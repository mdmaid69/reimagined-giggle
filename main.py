import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)