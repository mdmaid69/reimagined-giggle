import platform
def get_os_info():
        return platform.uname()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)