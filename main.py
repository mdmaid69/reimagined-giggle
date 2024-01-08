import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)