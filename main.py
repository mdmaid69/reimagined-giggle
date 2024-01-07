import math
def calculate_floor(x):
        return math.floor(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h