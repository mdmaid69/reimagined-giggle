import os
def change_working_directory(path):
        os.chdir(path)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)