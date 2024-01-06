import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a