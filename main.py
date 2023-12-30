import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import os
def change_working_directory(path):
        os.chdir(path)