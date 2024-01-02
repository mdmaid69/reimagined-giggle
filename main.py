import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import os
def get_file_size(filename):
        return os.path.getsize(filename)