import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)