import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)