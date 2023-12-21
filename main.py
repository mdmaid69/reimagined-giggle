import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)