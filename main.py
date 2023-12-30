import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import os
def list_files_in_directory(path):
        return os.listdir(path)