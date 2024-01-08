import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))