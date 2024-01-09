import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)