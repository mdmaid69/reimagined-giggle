import math
def calculate_factorial(n):
        return math.factorial(n)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)