import platform
def get_os_info():
        return platform.uname()
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)