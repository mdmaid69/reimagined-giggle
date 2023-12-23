import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a