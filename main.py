import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a