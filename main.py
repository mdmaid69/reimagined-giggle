import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a