import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a