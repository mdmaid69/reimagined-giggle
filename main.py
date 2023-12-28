import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)