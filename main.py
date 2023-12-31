import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)