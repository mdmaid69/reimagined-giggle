import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)