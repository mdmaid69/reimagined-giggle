import math
def calculate_factorial(n):
        return math.factorial(n)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a