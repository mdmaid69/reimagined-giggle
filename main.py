import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a