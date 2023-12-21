import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import sys
def print_python_version():
        return sys.version