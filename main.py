import os
def get_file_size(filename):
        return os.path.getsize(filename)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)