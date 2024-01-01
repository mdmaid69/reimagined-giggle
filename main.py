import os
def get_file_size(filename):
        return os.path.getsize(filename)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)