import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)