import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)