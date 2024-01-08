import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height