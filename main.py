import collections
def create_user_list():
        return collections.UserList()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h