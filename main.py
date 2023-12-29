import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)