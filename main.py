import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)