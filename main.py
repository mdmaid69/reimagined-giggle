import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)