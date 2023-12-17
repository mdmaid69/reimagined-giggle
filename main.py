import math
def calculate_sign(x):
        return math.copysign(1, x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a