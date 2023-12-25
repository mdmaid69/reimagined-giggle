import os
def remove_directory(path):
        os.rmdir(path)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)