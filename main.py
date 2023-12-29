import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import collections
def create_queue():
        return collections.deque()