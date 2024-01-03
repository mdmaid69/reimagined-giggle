import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h