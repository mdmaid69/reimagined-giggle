import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import platform
def get_os_info():
        return platform.uname()