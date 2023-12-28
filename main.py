import platform
def get_os_info():
        return platform.uname()
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)