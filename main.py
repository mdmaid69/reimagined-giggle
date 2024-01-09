import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))