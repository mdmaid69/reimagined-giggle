import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a