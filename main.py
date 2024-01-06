import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import platform
def get_os_info():
        return platform.uname()