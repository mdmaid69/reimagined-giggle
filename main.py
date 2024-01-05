import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)