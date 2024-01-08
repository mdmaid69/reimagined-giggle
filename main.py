n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"