import platform
def get_python_version():
        return platform.python_version()
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)