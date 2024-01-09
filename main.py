import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius