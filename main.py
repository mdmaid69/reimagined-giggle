import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h