import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))