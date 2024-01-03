import os
def get_environment_variable(var):
        return os.getenv(var)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)