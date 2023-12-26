import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)