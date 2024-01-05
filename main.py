import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import random
def roll_die():
        return random.randint(1, 6)