import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)