import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)