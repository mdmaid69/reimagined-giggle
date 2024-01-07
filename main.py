import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)