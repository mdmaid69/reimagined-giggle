import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)