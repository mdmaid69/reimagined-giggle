import math
def calculate_arc_cosine(x):
        return math.acos(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a