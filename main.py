import os
def remove_directory(path):
        os.rmdir(path)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)