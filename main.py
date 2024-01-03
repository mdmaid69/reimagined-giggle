import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)