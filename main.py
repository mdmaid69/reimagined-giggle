import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import sys
def print_python_version():
        print(sys.version)