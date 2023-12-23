import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)