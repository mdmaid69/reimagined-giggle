import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))