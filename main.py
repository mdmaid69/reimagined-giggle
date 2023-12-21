import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)