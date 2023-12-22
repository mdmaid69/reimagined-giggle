import os
def list_files_in_directory(path):
        return os.listdir(path)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)