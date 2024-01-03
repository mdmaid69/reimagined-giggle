import math
def calculate_circle_area(radius):
        return math.pi * radius**2
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a