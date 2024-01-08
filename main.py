import random
def generate_random_number(start, end):
        return random.randint(start, end)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)