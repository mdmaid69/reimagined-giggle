import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)