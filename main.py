import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a