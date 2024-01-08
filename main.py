import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)