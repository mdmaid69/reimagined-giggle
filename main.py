import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import os
def get_file_size(filename):
        return os.path.getsize(filename)