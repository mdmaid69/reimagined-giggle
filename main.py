import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import os
def change_working_directory(path):
        os.chdir(path)