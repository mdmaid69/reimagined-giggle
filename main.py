import math
def calculate_absolute_value(x):
        return math.fabs(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a