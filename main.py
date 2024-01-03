import os
def change_working_directory(path):
        os.chdir(path)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)