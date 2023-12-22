import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
n = 10
print("Cube numbers:", [x**3 for x in range(n)])