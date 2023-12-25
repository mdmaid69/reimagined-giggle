import math
def calculate_sign(x):
        return math.copysign(1, x)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)