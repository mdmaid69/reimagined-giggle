import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h