import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)