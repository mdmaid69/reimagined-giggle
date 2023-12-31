import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))