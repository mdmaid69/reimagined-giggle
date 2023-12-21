import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def greet(name):
        print(f"Hello, {name}!")