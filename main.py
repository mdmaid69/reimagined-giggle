import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)