import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import sys
def add_to_python_path(path):
        sys.path.append(path)