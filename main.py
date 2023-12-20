import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)