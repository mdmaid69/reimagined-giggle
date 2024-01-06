import glob
def find_files(pattern):
        return glob.glob(pattern)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)