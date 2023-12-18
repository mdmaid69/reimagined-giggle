import os
def remove_directory(path):
        os.rmdir(path)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)