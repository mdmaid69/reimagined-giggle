import sys
def add_to_python_path(path):
        sys.path.append(path)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h