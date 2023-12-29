import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)