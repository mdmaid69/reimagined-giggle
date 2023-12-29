import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)