import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}