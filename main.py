import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a