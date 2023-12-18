import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)