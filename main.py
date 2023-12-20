import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)