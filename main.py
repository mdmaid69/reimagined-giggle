import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a