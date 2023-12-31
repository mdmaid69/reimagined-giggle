import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))