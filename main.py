import os
def remove_directory(path):
        os.rmdir(path)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)