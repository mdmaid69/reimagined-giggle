import os
def change_working_directory(path):
        os.chdir(path)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h