import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a