import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)