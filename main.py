import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)