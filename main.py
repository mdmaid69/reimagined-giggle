import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import random
def generate_random_choice(choices):
        return random.choice(choices)