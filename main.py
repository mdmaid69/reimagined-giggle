import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import platform
def get_os_info():
        return platform.uname()