import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import glob
def find_files(pattern):
        return glob.glob(pattern)