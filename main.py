import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a