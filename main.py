import os
def get_file_size(filename):
        return os.path.getsize(filename)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)