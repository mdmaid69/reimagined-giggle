import os
def get_environment_variable(var):
        return os.getenv(var)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)