import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)