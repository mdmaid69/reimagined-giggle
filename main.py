import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))