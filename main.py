import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a