import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a