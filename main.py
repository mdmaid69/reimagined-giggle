import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import platform
def get_os_info():
        return platform.uname()