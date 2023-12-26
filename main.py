import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))