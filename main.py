import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)