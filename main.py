import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h