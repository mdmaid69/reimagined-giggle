import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import collections
def create_user_list():
        return collections.UserList()