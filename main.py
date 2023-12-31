import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)