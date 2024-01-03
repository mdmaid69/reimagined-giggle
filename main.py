import getpass
def get_username():
        return getpass.getuser()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)