import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)