import random
def roll_die():
        return random.randint(1, 6)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)