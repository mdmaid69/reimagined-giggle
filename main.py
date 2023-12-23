import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))