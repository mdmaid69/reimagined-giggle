import platform
def get_python_version():
        return platform.python_version()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h