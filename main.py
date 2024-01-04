import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import platform
def get_python_version():
        return platform.python_version()