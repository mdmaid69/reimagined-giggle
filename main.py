import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a