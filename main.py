import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)