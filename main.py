import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)