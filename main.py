import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import random
def roll_die():
        return random.randint(1, 6)