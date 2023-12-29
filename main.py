import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import random
def generate_random_number(start, end):
        return random.randint(start, end)