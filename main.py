import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))