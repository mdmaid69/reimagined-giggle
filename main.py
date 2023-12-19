import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import itertools
print(list(itertools.permutations([1, 2, 3])))