import os
def list_files_in_directory(path):
        return os.listdir(path)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)