import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import os
def get_file_size(filename):
        return os.path.getsize(filename)