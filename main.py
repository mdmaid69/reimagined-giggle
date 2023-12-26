import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)