import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import collections
def create_user_dict():
        return collections.UserDict()