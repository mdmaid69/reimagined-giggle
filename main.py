import math
def calculate_arc_sine(x):
        return math.asin(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a