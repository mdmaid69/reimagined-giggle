import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import platform
def get_python_version():
        return platform.python_version()