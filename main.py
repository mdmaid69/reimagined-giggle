import os
def get_environment_variable(var):
        return os.getenv(var)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)