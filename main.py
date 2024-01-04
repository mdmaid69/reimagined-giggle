import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h