import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import os
def list_files_in_directory(path):
        return os.listdir(path)