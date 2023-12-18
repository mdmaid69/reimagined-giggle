import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)