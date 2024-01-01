import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)