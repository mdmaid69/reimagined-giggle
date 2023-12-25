import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)