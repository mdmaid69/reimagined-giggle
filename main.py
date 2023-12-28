import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)