import math
def calculate_arc_sine(x):
        return math.asin(x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a