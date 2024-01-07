import os
def remove_directory(path):
        os.rmdir(path)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h