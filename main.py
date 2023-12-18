import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3