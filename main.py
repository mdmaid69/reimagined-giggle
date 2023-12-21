import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)