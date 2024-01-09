import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import sys
def print_python_version():
        return sys.version