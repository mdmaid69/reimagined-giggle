import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])