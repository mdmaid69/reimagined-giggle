import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)