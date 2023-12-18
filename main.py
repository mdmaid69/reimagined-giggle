import os
def change_working_directory(path):
        os.chdir(path)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)