import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)