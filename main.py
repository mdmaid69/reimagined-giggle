import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)