import os
def get_environment_variable(var):
        return os.getenv(var)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)