import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
n = 10
print("Square numbers:", [x**2 for x in range(n)])