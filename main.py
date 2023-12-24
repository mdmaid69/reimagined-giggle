import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h