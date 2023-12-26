import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import glob
def find_files(pattern):
        return glob.glob(pattern)