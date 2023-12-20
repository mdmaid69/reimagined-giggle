import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height