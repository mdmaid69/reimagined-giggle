import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))