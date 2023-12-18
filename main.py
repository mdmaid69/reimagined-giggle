import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import math
def calculate_permutations(n, k):
        return math.perm(n, k)