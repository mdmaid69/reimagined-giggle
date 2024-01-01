import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)