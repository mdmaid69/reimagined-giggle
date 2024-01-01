import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import sys
def add_to_python_path(path):
        sys.path.append(path)