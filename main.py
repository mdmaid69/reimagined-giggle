import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))