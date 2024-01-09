import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)