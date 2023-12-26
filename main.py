import math
def calculate_arc_cosine(x):
        return math.acos(x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a