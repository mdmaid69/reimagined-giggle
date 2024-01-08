import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a