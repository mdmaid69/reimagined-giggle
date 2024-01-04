import math
def calculate_absolute_value(x):
        return math.fabs(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h