import math
def calculate_arc_tangent(x):
        return math.atan(x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a