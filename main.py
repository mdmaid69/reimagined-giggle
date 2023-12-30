import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a