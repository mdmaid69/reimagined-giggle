import os
def get_file_size(filename):
        return os.path.getsize(filename)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h