import os
def remove_directory(path):
        os.rmdir(path)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)