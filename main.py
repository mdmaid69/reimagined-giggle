import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import glob
def find_files(pattern):
        return glob.glob(pattern)