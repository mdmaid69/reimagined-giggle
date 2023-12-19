import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)