import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import os
def change_working_directory(path):
        os.chdir(path)