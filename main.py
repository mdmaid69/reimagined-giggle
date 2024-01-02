import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)