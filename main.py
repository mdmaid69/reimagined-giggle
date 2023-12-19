n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"