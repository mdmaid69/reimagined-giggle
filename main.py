import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)