import glob
def find_files(pattern):
        return glob.glob(pattern)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)