import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height