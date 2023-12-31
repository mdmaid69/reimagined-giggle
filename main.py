import random
def roll_die():
        return random.randint(1, 6)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))