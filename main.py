import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import os
def get_current_working_directory():
        return os.getcwd()