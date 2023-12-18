import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)