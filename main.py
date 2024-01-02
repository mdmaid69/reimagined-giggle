import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import getpass
def get_username():
        return getpass.getuser()