import getpass
def get_username():
        return getpass.getuser()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)