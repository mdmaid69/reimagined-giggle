import os
def get_file_size(filename):
        return os.path.getsize(filename)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)