import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))