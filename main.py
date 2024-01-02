import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h