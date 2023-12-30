import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3