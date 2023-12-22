import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height