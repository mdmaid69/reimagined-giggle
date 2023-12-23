import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)