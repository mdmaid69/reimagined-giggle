import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import random
def generate_random_choice(choices):
        return random.choice(choices)