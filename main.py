import random
def generate_random_choice(choices):
        return random.choice(choices)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)