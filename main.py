import platform
def get_python_version():
        return platform.python_version()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)