import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)