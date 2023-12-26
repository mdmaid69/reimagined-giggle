import math
def calculate_inverse_hyperbolic_sine(x):
        return math.asinh(x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a