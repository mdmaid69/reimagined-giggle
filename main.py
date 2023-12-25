import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)