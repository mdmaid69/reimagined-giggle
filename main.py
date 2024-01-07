import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)