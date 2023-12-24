import os
def get_current_working_directory():
        return os.getcwd()
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)