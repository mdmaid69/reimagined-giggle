import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)