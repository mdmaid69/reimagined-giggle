import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height