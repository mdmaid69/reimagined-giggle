import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height