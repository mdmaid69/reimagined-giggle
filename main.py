import platform
def get_python_version():
        return platform.python_version()
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)