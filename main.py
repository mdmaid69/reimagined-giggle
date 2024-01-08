import os
def get_current_working_directory():
        return os.getcwd()
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)