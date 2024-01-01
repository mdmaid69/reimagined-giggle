import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"