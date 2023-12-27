import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a