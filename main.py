import collections
def create_ordered_dict():
        return collections.OrderedDict()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)