import collections
def create_user_dict():
        return collections.UserDict()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)