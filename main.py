import math
def calculate_circle_area(radius):
        return math.pi * radius**2
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a