import math
def calculate_sign(x):
        return math.copysign(1, x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h