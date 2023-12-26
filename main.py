import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))