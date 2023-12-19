import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)