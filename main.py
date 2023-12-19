import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))