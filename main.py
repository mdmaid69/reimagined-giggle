import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))