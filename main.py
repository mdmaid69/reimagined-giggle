import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)