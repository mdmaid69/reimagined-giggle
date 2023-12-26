import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height