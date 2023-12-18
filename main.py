import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a