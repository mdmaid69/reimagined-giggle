import os
def list_files_in_directory(path):
        return os.listdir(path)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)