import sys
def print_python_version():
        print(sys.version)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)