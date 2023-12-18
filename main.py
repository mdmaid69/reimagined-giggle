import os
def get_environment_variable(var):
        return os.getenv(var)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)