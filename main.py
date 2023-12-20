import collections
def create_ordered_dict():
        return collections.OrderedDict()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)