import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a