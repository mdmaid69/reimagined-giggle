import math
def calculate_sign(x):
        return math.copysign(1, x)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)