import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import os
def change_working_directory(path):
        os.chdir(path)