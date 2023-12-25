import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)