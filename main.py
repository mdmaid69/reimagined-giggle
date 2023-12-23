import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3