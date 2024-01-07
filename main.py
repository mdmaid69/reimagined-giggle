import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)