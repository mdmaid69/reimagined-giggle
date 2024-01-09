import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))