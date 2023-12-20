import os
def remove_directory(path):
        os.rmdir(path)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)