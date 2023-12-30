import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import glob
def find_files(pattern):
        return glob.glob(pattern)