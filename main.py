import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height