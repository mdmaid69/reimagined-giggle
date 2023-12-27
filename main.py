import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)