import collections
def create_stack():
        return collections.deque()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"