import os
def remove_directory(path):
        os.rmdir(path)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)