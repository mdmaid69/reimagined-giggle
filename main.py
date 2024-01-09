import math
def calculate_sine(x):
        return math.sin(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h