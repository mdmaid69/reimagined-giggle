import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)