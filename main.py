import getpass
def get_username():
        return getpass.getuser()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h