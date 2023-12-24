import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a