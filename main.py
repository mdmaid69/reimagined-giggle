import glob
def find_files(pattern):
        return glob.glob(pattern)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)