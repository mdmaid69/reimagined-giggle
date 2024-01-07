import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)