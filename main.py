import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import math
def calculate_combinations(n, k):
        return math.comb(n, k)