import glob
def find_files(pattern):
        return glob.glob(pattern)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)