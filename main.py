import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a