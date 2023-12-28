import collections
def create_user_dict():
        return collections.UserDict()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h