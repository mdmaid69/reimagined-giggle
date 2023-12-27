import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def convert_to_hex(n):
        return hex(n)