import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import math
def calculate_permutations(n, k):
        return math.perm(n, k)