import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)