import random
def roll_die():
        return random.randint(1, 6)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"