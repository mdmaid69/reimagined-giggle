import os
def list_files_in_directory(path):
        return os.listdir(path)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)