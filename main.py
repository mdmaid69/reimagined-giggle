import os
def list_files_in_directory(path):
        return os.listdir(path)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)