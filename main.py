import os
def list_files_in_directory(path):
        return os.listdir(path)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)