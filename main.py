import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
n = 10
print("Powers of 2:", [2**x for x in range(n)])