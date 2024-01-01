import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)