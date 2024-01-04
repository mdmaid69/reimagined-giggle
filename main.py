import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import platform
def get_os_info():
        return platform.uname()